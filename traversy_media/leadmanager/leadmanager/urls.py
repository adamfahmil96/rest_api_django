from django.contrib import admin
from django.urls import path, include

# kita melakukan set url global ini dengan url yang lain

urlpatterns = [
    path('', include('leads.urls')),
]
