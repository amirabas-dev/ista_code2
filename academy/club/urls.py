from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('member/', views.member),
    path('getinfo/<str:sname>', views.info),
    path('list/' , views.Liststudent.as_view()),
    path('list2/' , views.Liststudent2.as_view())
]
