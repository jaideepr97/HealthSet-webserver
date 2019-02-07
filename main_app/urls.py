from django.urls import path
from .views import ListPatientsView, patientOp, doctorOp, authenticateUser


urlpatterns = [
    # path('patients/', ListPatientsView.as_view(), name="patients-all")
    path('patients/', patientOp),
    path('doctors/', doctorOp),
    path('authenticate/', authenticateUser)
]
