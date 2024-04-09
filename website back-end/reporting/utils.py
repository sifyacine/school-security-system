from .models import StudentReport, StaffReport

def save_student_report(student, report_title, report_content, attachment=None):
    report = StudentReport(student=student, report_title=report_title, report_content=report_content)
    if attachment:
        report.attachment = attachment
    report.save()

def save_staff_report(staff, subject, message, attachment=None):
    report = StaffReport(staff=staff, subject=subject, message=message)
    if attachment:
        report.attachment = attachment
    report.save()