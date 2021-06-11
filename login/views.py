from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.

def index(request):
 if request.user.is_anonymous:
  return redirect("/")
 return render(request,"home.html")


def login(request):
 if request.method=="POST":
  email=request.POST.get('email')
  password=request.POST.get('password')
  user= authenticate(email=email,password=password)
  if user is not None:
   return render("/")
 else:

  return render(request,"login.html")

 return render(request,"login.html")


def logout(request):
 logout(request)
 return render (request,"home.html")
 