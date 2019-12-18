from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Language, Programmer, Paradigm
from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer

# Create your views here.

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # kalau mau edit harus login user utk model ini

class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer