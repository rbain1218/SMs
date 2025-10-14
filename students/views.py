from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Student

@login_required(login_url='/login/')
def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/students.html', {'students': students})
