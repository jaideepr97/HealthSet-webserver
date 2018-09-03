from django.db import models

class Patient(models.Model):

    patient_id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    age = models.IntegerField()

    class Meta:
        db_table = "patient"
