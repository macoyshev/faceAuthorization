from django.urls import path
from .import views


urlpatterns = [
    path('identify', views.identify, name='identifyPage'),
    path('', views.home, name='homePage')
]