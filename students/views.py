from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm  

@login_required(login_url='/login/')
def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/students.html', {'students': students})


@login_required(login_url='/login/')
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})


@login_required(login_url='/login/')
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit_student.html', {'form': form, 'student': student})


@login_required(login_url='/login/')
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('students_list')
    return render(request, 'students/delete_student.html', {'student': student})
