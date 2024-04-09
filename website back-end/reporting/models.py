from django.db import models
from registering.models import Student, Staff

class StudentReport(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    report_title = models.CharField(max_length=255)
    report_content = models.TextField()
    attachment = models.FileField(null=True, blank=True, upload_to='media/', default=None)

    def __str__(self):
        return self.report_title

class StaffReport(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    attachment = models.FileField(upload_to='media')

    def __str__(self):
        return self.subject