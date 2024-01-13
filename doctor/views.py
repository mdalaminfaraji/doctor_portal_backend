from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AvailableTimeSerializer, SpecializationSerializer, DesignationSerializer, DoctorSerializer, ReviewSerializer
from .models import Doctor, AvailableTime, Specialization, Designation, Review

class DoctorViewset(viewsets.ModelViewSet):
        queryset=Doctor.objects.all()
        serializer_class=DoctorSerializer
class AvailableTimeViewset(viewsets.ModelViewSet):
        queryset=AvailableTime.objects.all()
        serializer_class=AvailableTimeSerializer
class SpecializationViewset(viewsets.ModelViewSet):
        queryset=Specialization.objects.all()
        serializer_class=SpecializationSerializer
class DesignationViewset(viewsets.ModelViewSet):
        queryset=Designation.objects.all()
        serializer_class=DesignationSerializer
class ReviewViewset(viewsets.ModelViewSet):
        queryset=Review.objects.all()
        serializer_class=ReviewSerializer

# Create your views here.
