from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def info(request , sname):
    a = students.objects.filter(name = sname).values()
    return HttpResponse(a)

def member(request):
    return HttpResponse('Hello!')