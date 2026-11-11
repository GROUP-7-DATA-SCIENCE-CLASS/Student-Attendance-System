
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Student, Attendance
from .forms import StudentForm, AttendanceForm


def home(request):
    total_students = Student.objects.count()
    total_attendance = Attendance.objects.count()

    context = {
        'total_students': total_students,
        'total_attendance': total_attendance,
    }

    return render(request, 'attendance/home.html', context)


def student_list(request):
    students = Student.objects.all()

    context = {
        'students': students,
    }

    return render(request, 'attendance/student_list.html', context)


def student_create(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Student registered successfully!')
            return redirect('attendance:student_list')

    else:
        form = StudentForm()

    context = {
        'form': form,
    }

    return render(request, 'attendance/student_form.html', context)


def attendance_list(request):
    records = Attendance.objects.select_related('student').all()

    context = {
        'records': records,
    }

    return render(request, 'attendance/attendance_list.html', context)


def attendance_create(request):

    if request.method == 'POST':
        form = AttendanceForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Attendance recorded successfully!')
            return redirect('attendance:attendance_list')

    else:
        form = AttendanceForm()

    context = {
        'form': form,
    }

    return render(request, 'attendance/attendance_form.html', context)


