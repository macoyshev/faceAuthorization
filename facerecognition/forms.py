from .models import Student
from django.forms import ModelForm


class CreateStudent(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

