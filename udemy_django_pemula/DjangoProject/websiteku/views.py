from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def profil(request):
    return HttpResponse("Ini adalah halaman profil")