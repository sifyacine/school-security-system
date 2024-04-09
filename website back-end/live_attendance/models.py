from django.db import models

class Attendance(models.Model):
    is_staff = models.BooleanField(default=False)
    number = models.CharField(max_length=10)
    full_name = models.CharField(max_length=100)
    card_id = models.CharField(max_length=20)
    time_in = models.DateTimeField()
    time_out = models.DateTimeField(blank=True, null=True)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} ({self.number})"

