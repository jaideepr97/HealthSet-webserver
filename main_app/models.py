from django.db import models

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    age = models.IntegerField()
    qualification = models.TextField()
    address = models.TextField()
    number = models.IntegerField()

    class Meta:
        db_table = "doctor"

class Patient(models.Model):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    blood_group_choices = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-')
    )

    patient_id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    age = models.IntegerField()
    doctor = models.ForeignKey(Doctor, null = True, on_delete = models.SET_NULL)
    gender = models.CharField(max_length = 6, choices = gender_choices)
    blood_group = models.CharField(max_length = 3, choices = blood_group_choices)
    weight = models.IntegerField()
    height = models.IntegerField()
    diabetes = models.BooleanField()
    smoker = models.BooleanField()
    drinker = models.BooleanField()

    class Meta:
        db_table = "patient"
