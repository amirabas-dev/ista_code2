from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView

# Create your views here.

def info(request , sname):
    a = students.objects.filter(name = sname).values()
    return HttpResponse(a)

def member(request):
    return HttpResponse('Hello!')

#DRF Types : APIView
class Liststudent(APIView):
    def get(self, request):
        student = students.objects.all()
        serializer = studentSerializer(student, many=True)
        return Response(serializer.data)
    
#DRF Types : Generic Views
class Liststudent2(ListCreateAPIView):
    queryset = students.objects.all()
    serializer_class = studentSerializer