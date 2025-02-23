from django.contrib import admin
from django.urls import path, include
from administration import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('login', views.Login, name='login'),
    path('signup', views.SignUp, name='signup'),
]
