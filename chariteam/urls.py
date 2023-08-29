
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from django.urls import path,include
from . import views

app_name = "chariteam"
urlpatterns = [
   path('', views.home, name="home"),
   path('dash/', views.dash, name="dash"),
   path('pin/', views.pin, name="pin"),

   path('service/', views.service, name="service"),
   path('team/', views.team, name="team"),
   path('contacte/', views.contacte, name="contacte"),
   path('service/', views.service, name="service"),
   path('about/', views.about, name="about"),
   path('donate/', views.donate, name="donate"),
   path('contact/', views.contact, name="contact"),
   path('testimonial/', views.testimonial, name="testimonial"),
   path('error/', views.error, name="error"),

]