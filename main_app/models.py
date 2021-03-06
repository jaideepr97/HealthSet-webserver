from django.db import models

class Doctor(models.Model):
    patients = models.CharField(max_length = 100, default = '') #comma separated id's
    pending_requests = models.CharField(max_length = 100, default = '') #comma separated id's
    first_name = models.CharField(max_length = 50, default = '')
    last_name = models.CharField(max_length = 50, default = '')
    email = models.EmailField(unique = True, default = '')
    password = models.CharField(max_length = 50, default = '')
    age = models.IntegerField(default = 0)
    experience = models.IntegerField(default = 0)
    qualification = models.TextField(default = '')
    address = models.TextField(default = '')
    number = models.IntegerField(default = 0)
    fees = models.IntegerField(default = 0)
    gender = models.CharField(max_length = 50, default = '')


    def __str__(self):
        return self.email

    class Meta:
        db_table = "doctor"

class Patient(models.Model):
    doctor = models.CharField(max_length = 100, default = '', null = True) #single value
    first_name = models.CharField(max_length = 50, default = '')
    last_name = models.CharField(max_length = 50, default = '')
    email = models.EmailField(unique = True, default = '')
    password = models.CharField(max_length = 50, default = '')
    age = models.IntegerField(default = 0)
    gender = models.CharField(max_length = 6, default = '')
    blood_group = models.CharField(max_length = 3, default = '')
    weight = models.IntegerField(default = 0)
    height = models.IntegerField(default = 0)
    diabetes = models.BooleanField(default = False)
    smoker = models.BooleanField(default = False)
    drinker = models.BooleanField(default = False)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "patient"

class Data(models.Model):
    patient_id = models.IntegerField(default = 0)
    created = models.DateTimeField()
    ecg_url = models.URLField(max_length = 200)
    temperature = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "data"

class Chat(models.Model):
    doctor_id = models.IntegerField(default = 0)
    patient_id = models.IntegerField(default = 0)
    text = models.CharField(max_length = 100, default = '')
    sender = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "chat"
