# from rest_framework import serializers
# from .models import Patient, Doctor

# class PatientSerializer(serializers.ModelSerializer):
# 	doctors = serializers.PrimaryKeyRelatedField(many = True)

# 	class Meta:
# 		model = Patient
# 		fields = ("id", "first_name", "last_name", "email", "password", "age", "gender", "blood_group", "weight", "height", "diabetes", "smoker", "drinker", "doctors")

# class DoctorSerializer(serializers.ModelSerializer):

# 	class Meta:
# 		model = Doctor
# 		fields = ("id", "first_name", "last_name", "email", "age", "password", "experience", "qualification", "address", "number", "fees", "gender")