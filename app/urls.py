from . import models,views
from django.shortcuts import render
from django.urls import path
from . import views



urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('create/', views.create_student, name='create_student'),
    path('student/<slug:slug>/', views.student_detail, name='student_detail'),
    path('update/<slug:slug>/', views.update_student, name='update_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
]
