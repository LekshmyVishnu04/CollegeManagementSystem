from django.shortcuts import render, redirect
from .forms import TeacherModelForm
from .models import Teacher

# Create your views here.


def home(request, welcome):
    return render(request, 'teachers/teacherhome.html', {'welcome': welcome})


def list(request):
    data = Teacher.objects.all()
    return render(request, 'teachers/teacherlist.html', {'data': data})


def add(request):
    if request.method == 'POST':
        form = TeacherModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers:home', welcome='welcome')
    else:
        form = TeacherModelForm()
    return render(request, 'teachers/add.html', {'form': form})
