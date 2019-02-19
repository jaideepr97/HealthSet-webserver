from django.urls import path
from .views import getPatient, addPatient, getDoctor, addDoctor, authenticateUser, getAllDoctors, getChats, addChat, addData


urlpatterns = [
    path('getPatient/', getPatient),
    path('addPatient/', addPatient),
    path('getDoctor/', getDoctor),
    path('addDoctor/', addDoctor),
    path('getAllDoctors/', getAllDoctors),
    path('authenticate/', authenticateUser),
    path('getChats/', getChats),
    path('addChat/', addChat),
    path('addData/', addData),
]
