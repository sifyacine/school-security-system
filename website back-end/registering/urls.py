from django.urls import path
from . import views

app_name = 'registering'

urlpatterns = [
    path('add_student/', views.add_student, name='add_student'),
    path('add_staff/', views.add_staff, name='add_staff'),
]