# Generated by Django 2.0.8 on 2018-09-03 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_doctor_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='doctor',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
