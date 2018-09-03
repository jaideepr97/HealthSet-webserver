from django.urls import path
from .views import ListPatientsView, patientOp, doctorOp


urlpatterns = [
    # path('patients/', ListPatientsView.as_view(), name="patients-all")
    path('patients/', patientOp),
    path('doctors/', doctorOp),
]
