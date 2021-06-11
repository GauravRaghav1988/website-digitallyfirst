
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate

# Create your views here.

def sign_in(request):
 if request.method=="POST":
  user= authenticate(name="name",password1="password1")
  if user is not None:
    pass
  else:
   return render(request,"sign_in.html")