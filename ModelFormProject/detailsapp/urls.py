from django.urls import path
from django.contrib import admin

from detailsapp import views as detailsapp_views

urlpatterns = [
 path('userdetails/', detailsapp_views.userDetails),
 path('display/', detailsapp_views.userDetails),

path('', detailsapp_views.userDetails),
]
