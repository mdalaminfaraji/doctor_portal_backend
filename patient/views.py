from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .models import Patient
from .serializers import PatientSerializer

class PatientViewset(viewsets.ModelViewSet):
        queryset=Patient.objects.all()
        serializer_class=PatientSerializer
