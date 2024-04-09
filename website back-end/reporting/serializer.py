from rest_framework import serializers
from .models import StudentReport, StaffReport

class StudentReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentReport
        fields = ['student', 'report_title', 'report_content', 'attachment']

class StaffReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffReport
        fields = ['staff', 'subject', 'message', 'attachment']