from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout,login

def home(request):
 return render(request,"home.html")





def signin(request):
  if request.method=="POST":
   name=request.POST.get('name')
   password=request.POST.get('password')
   user = authenticate(name=name,password=password)
   print(name,password)
   if user is not None:
     login(request,user)
   return render(request,"/")
  else:
   return render(request,"signin.html")
  return render(request,"signin.html")


def logoutuser(request):
 logout(request)
 return redirect("html.home")