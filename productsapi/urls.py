from django.urls import path
from . import views

urlpatterns = [
    path('simpleapi/', views.simpleapi, name='simpleapi'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login')
]
