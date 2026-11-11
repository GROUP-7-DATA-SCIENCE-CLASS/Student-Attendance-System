
from django import forms
from .models import Student, Attendance


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            'student_id',
            'full_name',
            'email',
            'course'
        ]

        widgets = {
            'student_id': forms.TextInput(attrs={
                'placeholder': 'e.g. DS001'
            }),

            'full_name': forms.TextInput(attrs={
                'placeholder': 'Enter full name'
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter email address'
            }),

            'course': forms.TextInput(attrs={
                'placeholder': 'Enter course'
            }),
        }


class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance

        fields = [
            'student',
            'date',
            'status'
        ]

        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date'
            }),
        }
