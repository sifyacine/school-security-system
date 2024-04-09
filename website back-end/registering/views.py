from rest_framework import viewsets
from .serializer import  StaffSerializer
from .models import Student, Staff
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def add_student(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        card_id = data.get('card_id')
        father_first_name = data.get('fatherFirstName')
        father_last_name = data.get('fatherLastName')
        number = data.get('number')
        parents_email = data.get('parentsEmail')
        address = data.get('address')


        # Create a new student instance
        student = Student(
            full_name=f"{first_name} {last_name}",
            father_full_name=f"{father_first_name} {father_last_name}",
            card_id=card_id,
            number=number,
            parents_email=parents_email,
            address=address
        )

        # Save the student to the database
        student.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})

@csrf_exempt
def add_staff(request):
    if request.method == "POST":
        data = json.loads(request.body)
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        number = data.get("number")
        staff_email = data.get("email")
        card_id = data.get("card_id")
        gender = data.get("gender")
        address = data.get("address")

        # Create a new staff object
        staff = Staff(
            full_name=f"{first_name} {last_name}",
            number=number,
            staff_email=staff_email,
            card_id=card_id,
            gender=gender,
            address=address,
        )
        staff.save()

        return JsonResponse({"message": "Staff added successfully."})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})

