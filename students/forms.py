from django import forms
from .models import Student


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['studentname', 'classname', 'division']
        labels = {'studentname': 'Student Name',
                  'classname': 'Class Name',
                  'division': 'Division'}
