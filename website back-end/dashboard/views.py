from django.conf import settings
from registering.models import Student, Staff
from django.shortcuts import render, redirect, get_object_or_404
import face_recognition
import numpy as np
import base64
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def dashboard_list(request):
    if request.method == "GET":
        students = Student.objects.all()
        staff = Staff.objects.all()
        data = {
            "students": list(students.values()),
            "staff": list(staff.values()),
        }
        return JsonResponse(data)



faces_db = {}
def load_faces():
    encodings_dir_student = os.path.join(settings.MEDIA_ROOT, 'encodingsdb', 'student')
    encodings_dir_staff = os.path.join(settings.MEDIA_ROOT, 'encodingsdb', 'staff')
    if os.path.isdir(encodings_dir_student) and os.path.isdir(encodings_dir_staff):
        for encodings_dir in [encodings_dir_student, encodings_dir_staff]:
            for filename in os.listdir(encodings_dir):
                name, extension = os.path.splitext(filename)
                if extension == '.npy':
                    encoding_file = os.path.join(encodings_dir, filename)
                    try:
                        encoding = np.load(encoding_file)
                        if encoding.ndim == 1 and encoding.shape[0] == 128:
                            faces_db[name] = encoding
                            print("Loaded encoding for {}".format(name))
                        else:
                            print("Invalid encoding for {}: unexpected shape {}".format(name, encoding.shape))
                    except Exception as e:
                        print("Error loading encoding for {}: {}".format(name, e))
    else:
        print("Encodings directory not found")


def encode_face(image_path, name, is_staff=False):
    try:
        # Load the image
        image = face_recognition.load_image_file(image_path)
        # Find the face locations
        face_locations = face_recognition.face_locations(image)
        # Check if any faces were found
        if len(face_locations) == 0:
            error_message = "No faces found in image for {}".format(name)
            print(error_message)
            return None
        # Encode the faces
        face_encodings = face_recognition.face_encodings(image, face_locations)
        # Save the face encoding to a file
        if is_staff:
            encoding_path = os.path.join(settings.MEDIA_ROOT, 'encodingsdb\staff\\', name + '.npy')
        else:
            encoding_path = os.path.join(settings.MEDIA_ROOT, 'encodingsdb\student\\', name + '.npy')
        os.makedirs(os.path.dirname(encoding_path), exist_ok=True) # ensure the directory exists
        np.save(encoding_path, face_encodings[0])
        print("Encoded image for {}".format(name))
        # Save the encoding file to the staff/student's encodings_file field
        if is_staff:
            staff = Staff.objects.get(card_id=name)
            staff.encodings_file = encoding_path
            staff.save()
        else:
            student = Student.objects.get(card_id=name)
            student.encodings_file = encoding_path
            student.save()
        return face_encodings[0]
    except Exception as e:
        error_message = "Error encoding face for {}: {}".format(name, e)
        print(error_message)
        return None


def save_face(card_id, face_encoding, is_staff):
    encodings_dir = os.path.join(settings.MEDIA_ROOT, 'encodingsdb')
    if not os.path.isdir(encodings_dir):
        os.makedirs(encodings_dir)
    encoding_file = os.path.join(encodings_dir, "{}.npy".format(card_id))
    np.save(encoding_file, face_encoding)

    # Update the face_encoding field of the corresponding Student or Staff instance
    if is_staff:
        try:
            staff = Staff.objects.get(card_id=card_id)
            staff.face_encoding = encoding_file
            staff.save()
        except Staff.DoesNotExist:
            print("No staff found with card ID: {}".format(card_id))
    else:
        try:
            student = Student.objects.get(card_id=card_id)
            student.face_encoding = encoding_file
            student.save()
        except Student.DoesNotExist:
            print("No student found with card ID: {}".format(card_id))


def encode_images(request):
    # Get the card ID and is_staff from the query string parameter
    card_id = request.GET.get('card')
    is_staff = request.GET.get('is_staff')

    # If the card ID is not provided, return an error response
    if not card_id:
        return render(request, 'encoding.html', {'error_message': 'No card ID was provided.'})

    # Determine if the student is a staff member or a regular student
    if is_staff == 'True':
        student = get_object_or_404(Staff, card_id=card_id)

    else:
        student = get_object_or_404(Student, card_id=card_id)

    if request.method == 'POST':
        # Check if an image was uploaded
        if 'image' in request.FILES:
            # Get the uploaded image file
            image_file = request.FILES['image']
            # Save the image file to disk
            image_filename = os.path.join(settings.MEDIA_ROOT, 'images/', card_id + '.jpg')
            with open(image_filename, 'wb') as f:
                f.write(image_file.read())
        else:
            # Get the image data from the request
            image_data = request.POST.get('image_data')
            # If the image data is not provided, return an error response
            if not image_data:
                return render(request, 'encoding.html', {'error_message': 'No image data was provided.'})
            # Decode the image data
            try:
                image_data = base64.b64decode(image_data.split(',')[1])
            except:
                return render(request, 'encoding.html', {'error_message': 'Invalid image data.'})
            # Save the image data to a file
            image_filename = os.path.join(settings.MEDIA_ROOT, 'images/', card_id + '.jpg')
            with open(image_filename, 'wb') as f:
                f.write(image_data)

        # Encode the face and store it in the database
        encoding = encode_face(image_filename, card_id, is_staff=(is_staff=='True'))
        if encoding is None:
            return render(request, 'encoding.html', {'error_message': 'No faces found in image. Please try again.'})
        else:
            save_face(card_id, encoding, is_staff=(is_staff=='True'))

        # Redirect to the success page
        return redirect('dashboard_home')

    # If the request method is not POST, render the image capture/select page
    return render(request, 'encoding.html', {'student': student, 'card_id': card_id})
