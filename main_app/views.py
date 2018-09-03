from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.parsers import JSONParser
from .models import Patient
from .serializers import PatientSerializer

class ListPatientsView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

@csrf_exempt
def getPatients(request, version):
    if version == 'v1':
        if request.method == 'GET':
            serializer = PatientSerializer(Patient.objects.all(), many = True)
            response_data = {}
            response_data['status'] = 'success'
            response_data['data'] = serializer.data
            return JsonResponse(response_data, safe = False)
        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = PatientSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        response_data = {}
        response_data['status'] = 'failure'
        response_data['message'] = 'API version does not exist'
        return JsonResponse(response_data)
