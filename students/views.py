from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# Registration

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form':form})    



# Read
@login_required
def student_list(request):
    students=Student.objects.all()

    return render(request, 'students/student_list.html', {'students':students})


# Create

def add_student(request):
    form=StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Student Added Successfully")
        return redirect('student_list')


    return render (request, 'students/add_student.html', {'form':form})

# update
def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm(instance=student) 

    return render(request, 'students/update_student.html', {'form':form})       


# Delete

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
            student.delete()
            return redirect('student_list')

    
    
    return render(request, 'students/delete_student.html', {'student': student})