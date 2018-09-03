from django.urls import path
from .views import ListPatientsView


urlpatterns = [
    path('patients/', ListPatientsView.as_view(), name="patients-all")
]
