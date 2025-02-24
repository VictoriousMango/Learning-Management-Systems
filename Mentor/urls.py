from django.contrib import admin
from django.urls import path, include
from Mentor import views

urlpatterns = [
    path('', views.welcome),
    path('Welcome/', views.index),
    path('CreateNew/', views.CreateNew),
    path('MyCoureses/', views.MyCoureses),
    path('Assessments/', views.Assessments),
    path('Notifications/', views.Notifications)
]
