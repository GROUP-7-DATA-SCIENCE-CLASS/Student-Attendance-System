from django.shortcuts import render

from django.http import HttpResponse
from .models import Student, Attendance


def home(request):
    return HttpResponse(
        "<h1>Student Attendance Management System</h1>"
        "<p>Welcome to our attendance management application.</p>"
    )


def student_list(request):
    students = Student.objects.all()

    if not students:
        return HttpResponse("<h2>No students registered yet.</h2>")

    response = "<h1>Registered Students</h1>"
    response += "<ul>"
    for student in students:
        response += (
            f"<li>{student.student_id} - "
            f"{student.full_name} - "
            f"{student.course}</li>"
        )
    response += "</ul>"
    return HttpResponse(response)


def attendance_list(request):
    records = Attendance.objects.select_related('student').all()

    if not records:
        return HttpResponse("<h2>No attendance records available.</h2>")

    response = "<h1>Attendance Records</h1>"
    response += "<table border='1' cellpadding='8'>"
    response += """
        <tr>
            <th>Student ID</th>
            <th>Student Name</th>
            <th>Date</th>
            <th>Status</th>
        </tr>
    """
    for record in records:
        response += f"""
            <tr>
                <td>{record.student.student_id}</td>
                <td>{record.student.full_name}</td>
                <td>{record.date}</td>
                <td>{record.get_status_display()}</td>
            </tr>
        """
    response += "</table>"
    return HttpResponse(response)