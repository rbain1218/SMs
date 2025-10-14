from django.contrib import admin
from .models import ClassModel

@admin.register(ClassModel)
class ClassModelAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'section', 'class_teacher')
    search_fields = ('class_name',)
