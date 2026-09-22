from django.db import models

# Create your models here.


class Student(models.Model):
    studentname = models.CharField(max_length=50)
    classname = models.IntegerField()
    division = models.CharField(max_length=2)
