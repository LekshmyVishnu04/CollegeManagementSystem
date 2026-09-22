from django import forms
from .models import Teacher


class TeacherModelForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['teachername', 'department']
        labels = {'teachername': 'Teacher Name',
                  'department': 'Department'}
