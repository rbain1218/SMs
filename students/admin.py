from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'roll_number', 'email', 'class_assigned')
    search_fields = ('first_name', 'last_name', 'roll_number')
    list_filter = ('class_assigned',)
