from django.urls import path
from .views import patientOp, doctorOp, chatOp


urlpatterns = [
    # path('patients/', ListPatientsView.as_view(), name="patients-all")
    path('patients/', patientOp),
    path('doctors/', doctorOp),
    # path('chat/', chatOp),
]
