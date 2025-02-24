from django.shortcuts import render, redirect

# Create your views here.
def welcome(request):
    return redirect('Welcome/')

def index(request):
    return render(request, "Learner/index.html")

def BrowseCourses(request):
    return render(request, "Learner/BrowseCourses.html")

def MyCourses(request):
    return render(request, "Learner/MyCourses.html")

def Assessments(request):    
    return render(request, "Learner/Assessments.html")

def Notifications(request):
    return render(request, "Learner/Notifications.html")
