from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage , name = 'homepage'),
    path("search",views.search , name= 'search'),
    path("newhome",views.home , name='home'),
    path("admin_home",views.admin_home , name='admin_home'),

]