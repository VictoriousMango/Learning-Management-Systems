# Manulay Created
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate
from python_assets.Logger import logger
from administration.models import Users

# Create your views here.
def login(request):
    logger.debug("This is Login Page")
    return render(request, "login.html")

def login_post(request):
    logger.debug("This is Login Check Page")
    if request.method == "POST":
        logger.debug("This is POST Request")
        userName = request.POST.get("userName")
        password = request.POST.get("password")
        try:
            user = Users.objects.get(user_id=userName, password=password)
            logger.debug("User Found")
            if user.role == "Admin":
                logger.debug("User is Admin")
                return redirect("/admin")
            elif user.role == "Mentor":
                logger.debug("User is Mentor")
                return redirect("/mentor")
            elif user.role == "Student":
                logger.debug("User is Student")
                return redirect("/student")
            else:
                logger.debug("User is not Admin, Mentor or Student")
                return HttpResponse("User is not Admin, Mentor or Student")
        except Users.DoesNotExist:
            logger.debug("User Not Found")
            return redirect("/login")

def Admin(request):
    logger.debug("This is Admin Page")
    return HttpResponse("This is Admin Page")

def Mentor(request):
    logger.debug("This is Mentor Page")
    return HttpResponse("This is Mentor Page")

def Student(request):
    logger.debug("This is Student Page")
    return HttpResponse("This is Student Page")

def sign_up(request):
    logger.debug("This is Signup Page")
    return HttpResponse("This is Signup Page")