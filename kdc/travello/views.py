from django.shortcuts import render
from . models import Destination,Testimonials,News,Menus



# Create your views here.


def index(request):
    classact=(Menus.objects.values('menuname').filter(id=1))
    dests=Destination.objects.all()
    testimonials=Testimonials.objects.all()
    news=News.objects.all()
    menu=Menus.objects.all()

    return render(request,'index.html',{'dests':dests,'testimonials':testimonials,'news':news,'menus':menu,'classact':classact.get()})

def about(request):
    #dests=Menus.objects.all()
    classact=(Menus.objects.values('menuname').filter(id=2))
    menu=Menus.objects.all()

    return render(request,'about.html',{'menus':menu,'classact':classact.get()})


