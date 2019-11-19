from django.shortcuts import render

from .models import Profile, Language, Word, Connection
from .serializers import ProfileSerializer, LanguageSerializer, WordSerializer, ConnectionSerializer
from rest_framework import viewsets



class ProfileViewSet(viewsets.ModelViewSet):
    queryset =  Profile.objects.all() 
    serializer_class = ProfileSerializer

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
