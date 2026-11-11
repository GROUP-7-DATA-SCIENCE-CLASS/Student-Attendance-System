from django.contrib import admin
from .models import Student, Attendance


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'student_id',
        'full_name',
        'email',
        'course',
        'date_registered'
    )

    search_fields = (
        'student_id',
        'full_name',
        'email'
    )

    list_filter = ('course',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'date',
        'status',
        'recorded_at'
    )

    search_fields = (
        'student__student_id',
        'student__full_name'
    )

    list_filter = ('status', 'date')
