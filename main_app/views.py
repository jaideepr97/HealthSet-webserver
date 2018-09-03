from django.shortcuts import render
from rest_framework import generics
from .models import Patient
from .serializers import PatientSerializer

class ListPatientsView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
