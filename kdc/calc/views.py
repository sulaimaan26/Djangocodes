from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'maan'})

def add(request):
    val1 = request.POST['num1'] #output string type
    val2 = request.POST['num2']
    res  = int(val1) + int(val2)
    return render(request,'result.html',{'result':res})

    