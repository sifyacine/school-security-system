from rest_framework import serializers
from .models import Student, Staff

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('full_name', 'card_id', 'father_full_name', 'number', 'parents_email', 'address')

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('full_name', 'card_id', 'father_full_name', 'number', 'parents_email', 'address')