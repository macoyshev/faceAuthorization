from django.urls import path
from .import views


urlpatterns = [
    path('identify', views.identify, name='identifyPage'),
    path('create_student', views.create_student, name='create_studentPage'),
    path('', views.home, name='homePage')
]