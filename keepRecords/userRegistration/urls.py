from django.contrib import admin
from django.urls import path
from userRegistration.views import *

urlpatterns = [
    # path('',views.signIn,name='SignIn Page'),
    path('login',login,name='user_login'),
    path('users', fetch_users,name='all_list'),
    path('user/create',create_users,name='create_user'),
    path('user/delete',delete_users,name='delete_user')
]
