from django import forms
from .models import StudentReport, StaffReport

class StudentReportForm(forms.ModelForm):
    class Meta:
        model = StudentReport
        fields = ['student', 'report_title', 'report_content', 'attachment']
        widgets = {
            'report_content': forms.Textarea(attrs={'rows': 10}),
        }

class StaffReportForm(forms.ModelForm):
    class Meta:
        model = StaffReport
        fields = ['staff', 'subject', 'message', 'attachment']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 10}),
        }