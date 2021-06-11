from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.
def account(request):
 if request.user.is_anonymous:
  return redirect("/logins/")
 return render(request,"account.html")


 def logoutuser(request):
  logout(request)
 return redirect("html.home")