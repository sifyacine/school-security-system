from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'is_staff', 'number', 'full_name', 'card_id', 'time_in', 'time_out', 'is_present']