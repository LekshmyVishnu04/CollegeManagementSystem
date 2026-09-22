from django.db import models

# Create your models here.


class Teacher(models.Model):
    teachername = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
