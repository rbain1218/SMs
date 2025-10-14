from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ClassModel


@login_required(login_url='/login/')
def classes_list(request):
    classes = ClassModel.objects.all()
    return render(request, 'classes/classes.html', {'classes': classes})
