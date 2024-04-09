from django.urls import path
from .views import attendance, submit_attendance

urlpatterns = [
    path('', attendance, name='live_attendance'),
    path('submit_attendance/', submit_attendance , name='submit_attendance'),
]