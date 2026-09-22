from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('studlist/', views.studlist, name='studlist'),
    path('add/', views.add, name='add'),
    path('<str:welcome>/', views.studhome, name='home')
]
