from django import forms
from .models import Student, Staff

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('full_name', 'card_id', 'father_full_name', 'number', 'parents_email', 'address')
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter full name'}),
            'father_full_name': forms.TextInput(attrs={'placeholder': "Enter father's full name"}),
            'card_id': forms.TextInput(attrs={'placeholder': 'Enter card ID'}),
            'number': forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
            'parents_email': forms.EmailInput(attrs={'placeholder': 'Enter parents email'}),
            'address': forms.Textarea(attrs={'placeholder': 'Enter address'}),
        }
    def clean_number(self):
        number = self.cleaned_data.get('number')
        if number and (not number.isdigit() or len(number) != 10):
            raise forms.ValidationError('Phone number must be 10 digits')
        return number

    def clean_card_id(self):
        card_id = self.cleaned_data.get('card_id')
        if Student.objects.filter(card_id=card_id).exists():
            raise forms.ValidationError('Card ID must be unique')
        return card_id

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('full_name', 'number', 'staff_email', 'card_id', 'gender', 'address')
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter full name'}),
            'card_id': forms.TextInput(attrs={'placeholder': 'Enter card ID'}),
            'number': forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
            'staff_email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'gender': forms.Select(choices=Staff.GENDER_CHOICES),
            'address': forms.Textarea(attrs={'placeholder': 'Enter address'}),
        }
    def clean_number(self):
        number = self.cleaned_data.get('number')
        if number and (not number.isdigit() or len(number) != 10):
            raise forms.ValidationError('Phone number must be 10 digits')
        return number