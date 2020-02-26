from django.contrib import admin
from django.urls import path
from userRegistration.views import *

urlpatterns = [
    # path('',views.signIn,name='SignIn Page'),
    path('logIn',logIn,name='user_login')
]
