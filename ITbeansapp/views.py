from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
import random
# Create your views here.


from django.shortcuts import render
from django.contrib import admin
  

class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"