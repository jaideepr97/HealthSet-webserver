from django.urls import path
from .views import getPatient, addPatient, getDoctor, addDoctor, authenticateUser, getAllDoctors, getChats, addChat, addData, getData, analyzeECG, predictArrhythmia, getAllPendingRequests, acceptRequest, checkIfAccepted


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
    path('getData/', getData),
    path('analyzeECG/', analyzeECG),
    path('predictArrhythmia/', predictArrhythmia),
    path('getAllPendingRequests/', getAllPendingRequests),
    path('acceptRequest/', acceptRequest),
    path('checkIfAccepted/', checkIfAccepted),
]
