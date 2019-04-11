# Generated by Django 2.0.8 on 2019-04-11 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.IntegerField(default=0)),
                ('patient_id', models.IntegerField(default=0)),
                ('text', models.CharField(default='', max_length=100)),
                ('sender', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'chat',
            },
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.IntegerField(default=0)),
                ('created', models.DateTimeField()),
                ('ecg_url', models.URLField()),
                ('temperature', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
            options={
                'db_table': 'data',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patients', models.CharField(default='', max_length=100)),
                ('pending_requests', models.CharField(default='', max_length=100)),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=254, unique=True)),
                ('password', models.CharField(default='', max_length=50)),
                ('age', models.IntegerField(default=0)),
                ('experience', models.IntegerField(default=0)),
                ('qualification', models.TextField(default='')),
                ('address', models.TextField(default='')),
                ('number', models.IntegerField(default=0)),
                ('fees', models.IntegerField(default=0)),
                ('gender', models.CharField(default='', max_length=50)),
            ],
            options={
                'db_table': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(default='', max_length=100, null=True)),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=254, unique=True)),
                ('password', models.CharField(default='', max_length=50)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(default='', max_length=6)),
                ('blood_group', models.CharField(default='', max_length=3)),
                ('weight', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('diabetes', models.BooleanField(default=False)),
                ('smoker', models.BooleanField(default=False)),
                ('drinker', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'patient',
            },
        ),
    ]
