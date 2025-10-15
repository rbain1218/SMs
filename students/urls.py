
from django.urls import path
from . import views

urlpatterns = [
    path('', views.students_list, name='students_list'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
]
