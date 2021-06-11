from django.urls import path
from django.contrib import admin
from weather import views

urlpatterns = [
    path('',views.weather,name='weather')
]