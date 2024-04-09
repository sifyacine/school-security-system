from datetime import datetime
import winsound
import cv2
import os
import time
from django.shortcuts import redirect
import face_recognition
import numpy as np
from registering.models import Student, Staff
from .models import Attendance


def compare_encodings(encoding, encodingsdb_student_folder, encodingsdb_staff_folder):
    MATCH_THRESHOLD = 0.6
    # Load student encodings
    student_encodings = []
    for filename in os.listdir(encodingsdb_student_folder):
        if filename.endswith(".npy"):
            encoding_path = os.path.join(encodingsdb_student_folder, filename)
            student_encoding = np.load(encoding_path)
            student_encodings.append(student_encoding)

    # Load staff encodings
    staff_encodings = []
    for filename in os.listdir(encodingsdb_staff_folder):
        if filename.endswith(".npy"):
            encoding_path = os.path.join(encodingsdb_staff_folder, filename)
            staff_encoding = np.load(encoding_path)
            staff_encodings.append(staff_encoding)

    # Compare encoding with student encodings
    student_distances = face_recognition.face_distance(student_encodings, encoding)
    student_matches = np.nonzero(student_distances < MATCH_THRESHOLD)[0]
    if len(student_matches) > 0:
        match_filename = os.path.splitext(os.path.basename(os.listdir(encodingsdb_student_folder)[student_matches[0]]))[0]
        is_staff = False
        return match_filename, is_staff

    # Compare encoding with staff encodings
    staff_distances = face_recognition.face_distance(staff_encodings, encoding)
    staff_matches = np.nonzero(staff_distances < MATCH_THRESHOLD)[0]
    if len(staff_matches) > 0:
        match_filename = os.path.splitext(os.path.basename(os.listdir(encodingsdb_staff_folder)[staff_matches[0]]))[0]
        print(match_filename) 
        is_staff = True
        return match_filename, is_staff

    # No match found
    return None, None


def main():
    encodingsdb_student_folder = r'C:\Users\kal\Desktop\school_security_system\media\encodingsdb\student'
    encodingsdb_staff_folder = r'C:\Users\kal\Desktop\school_security_system\media\encodingsdb\staff'
    capture_delay = 5  # Delay in seconds before capturing and encoding next image

    cap = cv2.VideoCapture(0)
    while True:
        try:
            ret, frame = cap.read()
            cv2.imshow('Camera', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            face_locations = face_recognition.face_locations(frame)
            if len(face_locations) == 0:
                continue

            encoding = face_recognition.face_encodings(frame, face_locations)[0]

            # Capture image and save to media/images directory
            image_filename = f"captured_image.jpg"
            image_path = os.path.join('media', 'images', image_filename)
            cv2.imwrite(image_path, frame)

            # Encode image and save to media/encodings directory
            encoding_filename = f"captured_encoding.npy"
            encoding_path = os.path.join('media', 'encodings', encoding_filename)
            np.save(encoding_path, encoding)

            match_filename, is_staff = compare_encodings(encoding, encodingsdb_student_folder, encodingsdb_staff_folder)

            if match_filename:
                if is_staff:
                    print(f"Match found in staff database: {match_filename}")
                    try:
                        staff = Staff.objects.get(encodings_file=os.path.join(encodingsdb_staff_folder, f"{match_filename}.npy"))

                        attendance = Attendance()
                        attendance.number = staff.number
                        attendance.full_name = staff.full_name
                        attendance.card_id = staff.card_id
                        attendance.is_staff = True

                        attendance.time_in = datetime.now()
                        attendance.time_out = None
                        attendance.save()
                        print(f"Attendance recorded for {attendance.full_name} ({attendance.number}) at {attendance.time_in}")

                        # Delete captured image and encoding files
                        os.remove(image_path)
                        os.remove(encoding_path)

                        time.sleep(5)
                        return redirect('live_attendance')
                    except Staff.DoesNotExist:
                        print(f"No staff member found with {match_filename}")
                        continue
                else:
                    print(f"Match found in student database: {match_filename}")
                    try:
                        student = Student.objects.get(encodings_file=os.path.join(encodingsdb_student_folder, f"{match_filename}.npy"))

                        attendance = Attendance()
                        attendance.number = student.number
                        attendance.full_name = student.full_name
                        attendance.card_id = student.card_id
                        attendance.is_staff = False

                        attendance.time_in = datetime.now()
                        attendance.time_out = None
                        attendance.save()
                        print(f"Attendance recorded for {attendance.full_name} ({attendance.number}) at {attendance.time_in}")

                        # Delete captured image and encoding files
                        os.remove(image_path)
                        os.remove(encoding_path)

                        time.sleep(5)
                        return redirect('live_attendance')
                    except Student.DoesNotExist:
                        print(f"No student found with {match_filename}")
                        continue
            else:
                print("No match found in either database.")
                # Play a beep sound
                frequency = 2500  # Set frequency to 2500 Hz
                duration = 1000  # Set duration to 1000 ms (1 second)
                winsound.Beep(frequency, duration)

            # Delete captured image and encoding files
            os.remove(image_path)
            os.remove(encoding_path)

            time.sleep(capture_delay)  # Delay before capturing and encoding next image

        except Exception as e:
            print(f"Error: {e}")
            continue

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
