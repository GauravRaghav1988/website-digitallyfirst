from django.db import models

# Create your models here.
class Registration(models.Model):
  name=models.CharField(max_length=100)
  email=models.EmailField()
  password1=models.CharField(max_length=50)
  password2=models.CharField(max_length=100)


  def __str__(self):
   return self.name