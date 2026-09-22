from django.shortcuts import render, redirect
from .forms import StudentModelForm
from .models import Student

# Create your views here.


def studhome(request, welcome):
    return render(request, 'students/studenthome.html', {'message': welcome})


def studlist(request):
    data = Student.objects.all()
    return render(request, 'students/studlist.html', {'data': data})


def add(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:home', welcome='welcome')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})
