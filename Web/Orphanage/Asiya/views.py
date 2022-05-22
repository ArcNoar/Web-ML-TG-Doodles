
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render





def index(request):
    return render(request,'Orph_Pack/Main_Page.html', {'title' : 'Залл Приюта.'})

def About(request):
    return render(request,'Orph_Pack/About.html', {'title' : 'Досье.'})

def Admin(request):
    return render(request,'Orph_Pack/Admin.html', {'title' : 'Администрирование'})



def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1> Иди нахуй. </h1>')

