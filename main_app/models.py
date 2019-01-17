from django.db import models

class Doctor(models.Model):
    # doctor_id = models.AutoField()
    first_name = models.CharField(max_length = 50, default='') #done
    last_name = models.CharField(max_length = 50, default='')  #done
    email = models.EmailField(unique = True, default='')
    age = models.IntegerField(default=0)                    #done
    experience = models.IntegerField(default=0)             #done
    qualification = models.TextField(default='')             #done
    address = models.TextField(default='')
    number = models.IntegerField(default=0)                 #done
    fees = models.IntegerField(default=0)                   #done
    gender = models.CharField(max_length = 50, default='')     #done

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

    # patient_id = models.AutoField()
    first_name = models.CharField(max_length = 50, default='')
    last_name = models.CharField(max_length = 50, default='')
    email = models.EmailField(unique = True, default='')
    age = models.IntegerField(default=0)
    doctor = models.ForeignKey(Doctor, null = True, on_delete = models.SET_NULL)
    gender = models.CharField(max_length = 6, default='')
    blood_group = models.CharField(max_length = 3, default='')
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    diabetes = models.BooleanField(default=False)
    smoker = models.BooleanField(default=False)
    drinker = models.BooleanField(default=False)

    class Meta:
        db_table = "patient"
