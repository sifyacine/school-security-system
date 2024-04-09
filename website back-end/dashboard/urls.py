from django.urls import path
from .views import dashboard_list

urlpatterns = [
    path("student_list/", dashboard_list, name="student_list"),
]