from django.urls import path
from .views import ListPatientsView, getPatients


urlpatterns = [
    # path('patients/', ListPatientsView.as_view(), name="patients-all")
    path('patients/', getPatients)
]
