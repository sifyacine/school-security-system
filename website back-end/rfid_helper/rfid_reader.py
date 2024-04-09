import datetime 
import time
import serial
from live_attendance.models import Attendance
from registering.models import Staff, Student

# ser = serial.Serial('COM7', 9600)
ser = 0

def read_rfid():
    while True:
        if ser.in_waiting > 0:
            tagID = ser.readline().decode().rstrip()
            uid = tagID.replace(' ', '')
            print(uid)
            # Loop through students and check for a match
            students_data = Student.objects.all()
            for student in students_data:
                if uid == student.card_id:
                    print(f'Match found for student: {student.full_name}')
                    
                    # Update student's time_out
                    attendance = Attendance.objects.filter(card_id=uid).last()
                    if attendance:
                        attendance.time_out = datetime.datetime.now()
                        attendance.save()
                        print(f'Updated time_out for {attendance.card_id}')
                        
            # Loop through staff and check for a match
            staff_data = Staff.objects.all()
            for staff in staff_data:
                if uid == staff.card_id:
                    print(f'Match found for staff: {staff.full_name}')
                    
                    # Update staff's time_out
                    attendance = Attendance.objects.filter(card_id=uid).last()
                    if attendance:
                        attendance.time_out = datetime.datetime.now()
                        attendance.save()
                        print(f'Updated time_out for {attendance.card_id}')
            time.sleep(2)
        else: 
            print('Error')