from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def member(request):
    return HttpResponse('Hello!')