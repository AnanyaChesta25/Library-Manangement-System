from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_rental/<int:book_id>',views.add_rental, name="addrental"),
    path('open_rental/<int:book_id>',views.open_rental, name="rental"),
    path('show_rental/',views.show_rental, name="show_rental"),
    path('renter_list/', views.renter_list, name='renter_list')

]