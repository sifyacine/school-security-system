from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=255)
    father_full_name = models.CharField(max_length=255, default='')
    card_id = models.CharField(max_length=50, unique=True, null=False, blank=False)
    number = models.CharField(max_length=20)
    parents_email = models.EmailField()
    address = models.TextField()
    encodings_file = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    

    def __str__(self):
        return self.full_name

class Staff(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        )
    full_name = models.CharField(max_length=255)
    number = models.CharField(max_length=20)
    staff_email = models.EmailField(default='')
    card_id = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()
    encodings_file = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name
