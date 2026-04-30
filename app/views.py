from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.views.generic import DetailView


# Create your views here.

def student_list(request):
    students = Student.objects.all()
    return render(request, 'user_view.html', {'students': students})

def create_student(request):
    form = StudentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'create_user.html', {'form': form})



def student_detail(request, slug):
    student = get_object_or_404(Student, slug=slug)
    return render(request, 'user_view.html', {'student': student})

def update_student(request, slug):
    student = get_object_or_404(Student, slug=slug)

    if request.POST:
        student.name = request.POST.get('name')
        student.surename = request.POST.get('sure_name')
        student.age = request.POST.get('age')
        student.email = request.POST.get('email')
        student.phone_number = request.POST.get('phone_number')

        # if request.FILES.get('picture'):
        student.picture = request.FILES.get('picture')

        student.save()
        return redirect('student_detail', slug=student.slug)

    return render(request, 'update_user.html', {'student': student})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')



