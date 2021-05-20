from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    photo = models.ImageField()

    def __str__(self):
        return self.name
