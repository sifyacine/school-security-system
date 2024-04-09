from django.urls import path
from reporting.views import add_staff_report, add_student_report

name1 = 'staff_reports'
name2 = 'student_reports'

urlpatterns = [
    path('staff_reports', add_staff_report, name=name1),
    path('student_reports', add_student_report, name=name2),
]