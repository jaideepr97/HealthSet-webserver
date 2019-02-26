from django.contrib import admin
from .models import Patient, Doctor, Chat, Data

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Chat)
admin.site.register(Data)
