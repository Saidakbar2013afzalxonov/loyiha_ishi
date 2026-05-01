from django.contrib import admin
from . import models
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age', 'email', 'phone_number', 'created_at')
    search_fields = ('name', 'surname', 'email')
    list_filter = ('age',)
