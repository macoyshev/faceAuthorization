from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    photo = models.ImageField(upload_to='images', null=True)
    password = models.CharField(max_length=200, null=True)
    login = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.name} {self.surname}'
