from django.shortcuts import render, HttpResponse
from python_assets.Logger import logger

# Create your views here.
def Home(request):
    logger.debug("This is Home Page of Administration")
    return HttpResponse("This is Home Page")
def Login(request):
    logger.debug("This is Login Page of Administration")
    return HttpResponse("This is Login Page")

def SignUp(request):
    logger.debug("This is Signup Page of Administration")
    return HttpResponse("This is Signup Page")