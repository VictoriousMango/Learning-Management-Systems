from django.shortcuts import render, redirect
from administration.models import Users, Assessments, Courses
from python_assets.Logger import logger

# Create your views here.
def welcome(request):
    return redirect('Welcome/')

def index(request):
    return render(request, 'Mentor/index.html') 

def CreateNew(request):
    return render(request, 'Mentor/CreateNew.html')

def MyCoureses(request):
    CourseList = Courses.objects.filter(course_incharge_id = request.session["user_id"])
    logger.debug(CourseList)
    context = {
        'CourseList': CourseList
    }
    return render(request, 'Mentor/MyCourses.html', context=context)

def CourseManagement(request):
    if request.method == 'POST':
        CoursesList = Courses.objects.get(course_id = request.POST.get('course_id'))
        context = {
            'Resources': CoursesList.resources,
            'course_id' : CoursesList.course_id
        }
        if request.POST.get('action') == 'delete':
            del CoursesList.resources[request.POST.get('row_id')]
            CoursesList.save()
        elif request.POST.get('action') == 'create':
            CoursesList.resources[request.POST.get('resource_id')] = {
                "Title" : request.POST.get('Title'),
                "link" : request.POST.get('link')
            }
            CoursesList.save()
        elif request.POST.get('action') == 'update':
            CoursesList.resources[request.POST.get('resource_id')] = {
                "Title" : request.POST.get('Title'),
                "link" : request.POST.get('link')
            }
            CoursesList.save()
            

    return render(request, 'Mentor/CourseManagement.html', context=context)

def Assessments(request):
    return render(request, 'Mentor/Assessments.html')

def Notifications(request):
    return render(request, 'Mentor/Notifications.html')
