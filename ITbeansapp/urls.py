from django.urls import re_path, path
from ITbeansapp import views

from django.urls import path
from . import views

urlpatterns = [
    re_path(r'^$', views.HomePageView.as_view(), name = 'home'),
    path('about/', views.AboutPageView.as_view(), name = 'about')

]                                                       

