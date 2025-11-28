from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("register",views.register , name='register'),
    path("login",views.login_page , name= 'login'),
    path("myprofile", views.myprofile_page , name= 'profile')

]