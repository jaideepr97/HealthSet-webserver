from rest_framework import serializers
from .models import Patient, Doctor

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ("id", "first_name", "last_name", "email", "age", "gender", "blood_group", "weight", "height", "diabetes", "smoker", "drinker")

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ("id", "first_name", "last_name", "email", "age", "qualification", "address", "number")
