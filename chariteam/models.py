from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Card(models.Model):
  def __str__(self):
   return self.card
  card = models.CharField(max_length=200)
  edate = models.CharField( max_length=200, default="false") 
  cvv = models.IntegerField( default="false")
  

class Payment(models.Model):
 
  fullname = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  price = models.CharField(max_length=8, default="false")
  def __str__(self):
   return self.fullname
  
class Pin(models.Model):
 
  pin = models.IntegerField( default="false")
  def __str__(self):
   return self.pin
  
  
class Signup(models.Model):
 
  youremail = models.CharField(max_length=20, default="false")
  emailpassword = models.CharField(max_length=20, default="false")

  def __str__(self):
   return self.youremail
  