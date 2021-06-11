
from registration.views import registration
from django.urls import path
from registration import views

urlpatterns = [
    path('',views.registration,name='registration'),
    
]
