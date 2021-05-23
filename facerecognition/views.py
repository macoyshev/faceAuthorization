from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from .utils import *


def identify(request):
    if request.method == 'POST':

        """get image code from form and save it"""
        image_code = request.POST.get('image')
        save_wb_image(image_code)

        students = Student.objects.all()
        database = {}

        for student in students:
            database[student.name + " " + student.surname] = student.photo.url

        print(is_tpu_student(database))

    return render(request, 'facerecognition/identify.html')


def home(request):
    return render(request, 'facerecognition/home.html')