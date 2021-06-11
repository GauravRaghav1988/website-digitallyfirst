from django import contrib
from django.http.response import HttpResponse
from registration.models import Registration
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from . models import Registration



def registration(request):
 if request.method=="POST":
  name=request.POST.get("name")
  email=request.POST.get("email")
  password1=request.POST.get("password1")
  password2=request.POST.get("password2")
  registration= Registration(name=name,email=email,password1=password1,password2=password2)
  if password1==password2:
   registration.save()
  else:
   return redirect("/registration/",{"res":"Password not matching"})
 return render(request,'registration.html')