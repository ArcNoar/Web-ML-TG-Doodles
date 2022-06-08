
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *








def index(request):
    return render(request,'Orph_Pack/Main_Page.html', {'title' : 'Залл Приюта.'})

def About(request):
    return render(request,'Orph_Pack/About.html', {'title' : 'Досье.'})

def Admin(request):
    return render(request,'Orph_Pack/Admin.html', {'title' : 'Администрирование'})

def Login(request):
    return render(request,'Orph_Pack/Login.html', {'title' : 'Авторизация'})



def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1> Иди нахуй. </h1>')

