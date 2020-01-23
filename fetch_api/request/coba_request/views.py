from django.shortcuts import render
from django.http import HttpResponse
import requests

headers = {
    'Authorization': 'token 855a6d91dc69ed2:5a5095c82bfd4fe',
    'Content-Type': 'application/json',
}

def index(request):
    response = requests.get('http://168.168.168.100/api/resource/Patient?fields=["medical_record_number", "patient_name", "sex", "address"]', headers=headers)
    return HttpResponse(response.content)
