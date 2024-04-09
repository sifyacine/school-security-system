from .models import Staff, Student


def save_staff(full_name, number, staff_email, card_id, gender, address):
    staff = Staff.objects.create(full_name=full_name, number=number, card_id=card_id,  staff_email=staff_email, gender=gender, address=address)
    return staff

def save_student(full_name, card_id, number, father_full_name, parents_email, address):
    student = Student.objects.create(full_name=full_name, father_full_name=father_full_name, card_id=card_id, number=number, parents_email=parents_email, address=address)
    return student