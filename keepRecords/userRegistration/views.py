from django.shortcuts import render
from django.http import HttpResponse
from userRegistration.models import Person
# Create your views here.

def logIn(request):
    if request.method == 'POST':
        user_name = request.POST['Email']
        password = request.POST['Password']
    return HttpResponse('{"user_name" : "User_Name"}')

def logOut(request):
    return HttpResponse('LogOut...')
