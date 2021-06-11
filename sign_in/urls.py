
from django.urls import path
from sign_in import views

urlpatterns = [
    path('',views.sign_in,name='sign_in')
]
