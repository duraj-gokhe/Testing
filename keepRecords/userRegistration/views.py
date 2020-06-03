from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from userRegistration.models import Person
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from rest_framework import serializers

#Login on the application after registration
@csrf_exempt
def login(request):
    if request.method == 'POST':
            response = json.loads(request.body.decode('utf-8'))
            username = response.get('username')
            password = response.get('password')
            user = Person.objects.get(UserName = username)
            if Person.objects.filter(UserName = username) and Person.objects.filter(Password=password):
                context = {"success":True, "personId":user.id}
            else:           
                context = {"success":False, "error":[{"status":"Username or password wrong"}]}
                return JsonResponse(context,content_type='application/json; charset=utf-8',status=401)
            return JsonResponse(context, content_type='application/json; charset=utf-8')

#user creation/signup/registration/user update
@csrf_exempt
def create_users(request):
    if request.method == 'PUT':
        if request.GET.get('id'):
            response = json.loads(request.body.decode('utf-8'))
            first_name = response.get('firstname')
            last_name = response.get('lastname')
            user_id = request.GET.get('id')
            user = Person.objects.filter(id=user_id).update(FirstName = first_name, LastName= last_name,LastUpdateDateTime = datetime.now())
            context = {"Message":"User details successfully Updated"}
            return JsonResponse(context, content_type= 'application/json')
    if request.method == 'POST':
        response = json.loads(request.body.decode('utf-8'))
        first_name = response.get('firstname')
        last_name = response.get('lastname')
        username = response.get('username')
        email = response.get('email')
        password = response.get('password')
        if Person.objects.filter(UserName = username) or Person.objects.filter(Email = email):
            context = {"Message":"User name or email already exist"}
            return JsonResponse(context, content_type= "application/json")
        else:
            create_user = Person(FirstName = first_name, LastName = last_name, UserName = username, Email = email, Password = password)
            create_user.save()
            user = Person.objects.get(UserName = username)
            if Person.objects.filter(UserName = username) and Person.objects.filter(Password = password):
                context = {"success":True,"Person_id":user.id}
            return JsonResponse(context,content_type='application/json', status = 200)

#users fetch by name only
def fetch_users(request):
    if request.method == 'GET':
        user_list = Person.objects.filter().order_by('CreateDateTime')
        page = request.GET.get('page',1)
        paginator = Paginator(user_list,5)
        users = paginator.page(page)
        # for user in user_list:
            # details.append(str(user))
        context = {"success":True, "data":users}
    return JsonResponse(context,content_type= 'application/json',status=200,safe=False)


# Delete user by Id
def delete_users(request):
    if request.method == 'GET':
        user_name = request.GET.get('username')
        user_id = request.GET.get('id')
        user = Person.objects.get(id=user_id).delete()
        context = {"Message":"User deleted successfully!!!"}
        return JsonResponse(context,content_type= 'application/json')


        


