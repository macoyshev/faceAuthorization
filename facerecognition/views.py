from django.shortcuts import render
from django.shortcuts import redirect
from .utils import *
import PIL
import base64
from io import BytesIO


def index(request):
    if request.method == 'POST':
        data = request.POST.get('image')
        data = base64.b64decode(data)
        img0 = 'facerecognition/media/testim.bmp'
        with open(img0, 'wb') as f:
            f.write(data)
            f.close()
        img1 = PIL.Image.open(img0)
        context = {
            'image': img1
        }
        return render(request, 'facerecognition/worl.html', context)
    return render(request, 'facerecognition/main.html')

