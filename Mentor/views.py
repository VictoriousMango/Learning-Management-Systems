from django.shortcuts import render, redirect

# Create your views here.
def welcome(request):
    return redirect('Welcome/')

def index(request):
    return render(request, 'Mentor/index.html') 

def CreateNew(request):
    return render(request, 'Mentor/CreateNew.html')

def MyCoureses(request):
    return render(request, 'Mentor/MyCourses.html')

def Assessments(request):
    return render(request, 'Mentor/Assessments.html')

def Notifications(request):
    return render(request, 'Mentor/Notifications.html')
