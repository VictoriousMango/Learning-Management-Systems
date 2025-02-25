from django.shortcuts import render, redirect
from administration.models import Users, Courses, Assessments, Submissions

# Create your views here.
def welcome(request):
    return redirect('Welcome/')

def index(request):
    return render(request, "Learner/index.html")

def BrowseCourses(request):
    CoursesList = Courses.objects.all()
    for i in CoursesList:
        print(i.title)
        print(i.description)
        print(i.course_incharge_id)
        print(i.LandingPicture)
    context = {
        'CoursesList': CoursesList
    }
    return render(request, "Learner/BrowseCourses.html" , context=context)

def MyCourses(request):
    return render(request, "Learner/MyCourses.html")

def Assessments(request):    
    return render(request, "Learner/Assessments.html")

def Notifications(request):
    return render(request, "Learner/Notifications.html")
