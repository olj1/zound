from django.shortcuts import render
from .models import Entries
from .serializers import CedictionarySerializer
from rest_framework import viewsets

class CedictionaryViewSet(viewsets.ModelViewSet):
    queryset = Entries.objects.all()
    serializer_class = CedictionarySerializer
