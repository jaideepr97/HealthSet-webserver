# Generated by Django 2.0.8 on 2018-09-16 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_auto_20180916_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='message',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='patient',
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
