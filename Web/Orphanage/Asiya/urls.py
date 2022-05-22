from django.contrib import admin
from django.urls import path


from .views import *

urlpatterns = [
    path('',index,name='Main'),
    path('Admin/',Admin,name='Admin'),
    path('About/',About,name='About'),

    ]


handler404 = pageNotFound

