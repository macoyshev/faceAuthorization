from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from .utils import *
from .forms import CreateStudent


def identify(request):
    if request.method == 'POST':

        """get image code from form and save it"""
        image_code = request.POST.get('image')
        save_wb_image(image_code)

        students = Student.objects.all()

        student = is_tpu_student(students)
        if student:
            context = {
                'student': student,
            }

            return render(request, 'facerecognition/home.html', context=context)

    return render(request, 'facerecognition/identify.html')


def home(request):
    return render(request, 'facerecognition/home.html')


def create_student(request):
    form = CreateStudent()
    if request.method == 'POST':
        form = CreateStudent(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/identify')
    context = {
        'forms': form
    }
    return render(request, 'facerecognition/create_student.html', context)

