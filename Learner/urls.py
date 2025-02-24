from django.contrib import admin
from django.urls import path, include
from Learner import views

urlpatterns = [
    path("", views.welcome),
    path("Welcome/", views.index),
    path("BrowseCourses/", views.BrowseCourses),
    path("MyCourses/", views.MyCourses),
    path("Assessments/", views.Assessments),
    path("Notifications/", views.Notifications)
]
