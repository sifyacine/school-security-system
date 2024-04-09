from django.contrib import admin
from reporting.models import StaffReport, StudentReport

admin.site.register(StudentReport)
admin.site.register(StaffReport)
