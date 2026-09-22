from django.urls import path
from . import views

app_name = 'teachers'

urlpatterns = [
    path('list/', views.list, name='list'),
    path('add', views.add, name='add'),
    path('<str:welcome>/', views.home, name='home')

]
