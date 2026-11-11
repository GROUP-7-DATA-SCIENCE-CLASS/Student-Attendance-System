from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('attendance/', views.attendance_list, name='attendance_list'),
]