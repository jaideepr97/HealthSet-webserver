from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.parsers import JSONParser
from .models import Patient, Doctor, Chat, Data
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import IntegrityError
import heartpy as hp
import urllib.request

@csrf_exempt
def authenticateUser(request, version):
    response_data = {}
    if version == 'v1':
        if request.method == 'POST':
            print(request.POST.get('username'))
            user = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))
            if user is not None:
                response_data['status'] = 'success'
            else:
                response_data['status'] = 'failure'
            return JsonResponse(response_data, safe = False)
        else:
            response_data['status'] = "error"
            response_data['message'] = "invalid request"
        return JsonResponse(response_data)
    else:
        response_data['status'] = 'failure'
        response_data['message'] = 'API version does not exist'
        return JsonResponse(response_data)

@csrf_exempt
def getPatient(request, version):
    response_data = {}
    if version == "v1":
        if request.method == "GET":
            patient_id = request.GET["patient_id"]
            data = Patient.objects.filter(id = patient_id)
            response_data['status'] = "success"
            response_data['data'] = list(data.values())
        else:
            response_data['status'] = "error"
            response_data['message'] = "invalid request"
        return JsonResponse(response_data)
    else:
        response_data['status'] = 'failure'
        response_data['message'] = 'API version does not exist'
        return JsonResponse(response_data)

@csrf_exempt
def getDoctor(request, version):
    response_data = {}
    if version == "v1":
        if request.method == "GET":
            doctor_id = request.GET["doctor_id"]
            data = Doctor.objects.filter(id = doctor_id)
            response_data['status'] = "success"
            response_data['data'] = list(data.values())
        else:
            response_data['status'] = "error"
            response_data['message'] = "invalid request"
        return JsonResponse(response_data)
    else:
        response_data['status'] = 'failure'
        response_data['message'] = 'API version does not exist'
        return JsonResponse(response_data)

@csrf_exempt
def addPatient(request, version):
    response_data = {}
    if version == 'v1':
        if request.method == "POST":
            p = Patient(first_name = request.POST["first_name"], last_name = request.POST["last_name"], email = request.POST["email"], password = request.POST["password"], age = request.POST["age"], gender = request.POST["gender"], blood_group = request.POST["blood_group"], weight = request.POST["weight"], height = request.POST["height"], diabetes = request.POST["diabetes"], smoker = request.POST["smoker"], drinker = request.POST["drinker"])
            try:
                user = User.objects.create_user(username = request.POST["email"].split("@")[0], email = request.POST["email"], password = request.POST["password"], first_name = request.POST["first_name"], last_name = request.POST["last_name"])
                user.save()
                p.save()
                response_data['status'] = "success"
                response_data['data'] = p.id
            except IntegrityError as e:
                response_data['status'] = "error"
                response_data['message'] = "account exists"
        else:
            response_data['status'] = "error"
            response_data['message'] = "invalid request"
        return JsonResponse(response_data)
    else:
        response_data['status'] = 'failure'
        response_data['message'] = 'API version does not exist'
        return JsonResponse(response_data)

@csrf_exempt
def addDoctor(request, version):
    response_data = {}
    if version == 'v1':
        if request.method == "POST":
            d = Doctor(first_name = request.POST["first_name"], last_name = request.POST["last_name"], email = request.POST["email"], password = request.POST["password"], age = request.POST["age"], gender = request.POST["gender"], experience = request.POST["experience"], qualification = request.POST["qualification"], address = request.POST["address"], number = request.POST["number"], fees = request.POST["fees"])
            try:
                user = User.objects.create_user(username = request.POST["email"].split("@")[0], email = request.POST["email"], password = request.POST["password"], first_name = request.POST["first_name"], last_name = request.POST["last_name"])
                user.save()
                d.save()
                response_data['status'] = "success"
                response_data['data'] = d.id
            except IntegrityError as e:
                response_data['status'] = "error"
                response_data['message'] = "account exists"
        else:
            response_data['status'] = "error"
            response_data['message'] = "invalid request"
        return JsonResponse(response_data)
    else:
        response_data['status'] = 'failure'
        response_data['message'] = 'API version does not exist'
        return JsonResponse(response_data)

@csrf_exempt
def getAllDoctors(request, version):
    response_data = {}
    if version == 'v1':
        if request.method == "GET":
            data = Doctor.objects.all()
            response_data['status'] = "success"
            response_data['data'] = list(data.values())
        else:
            response_data['status'] = "error"
            response_data['message'] = "invalid request"
        return JsonResponse(response_data)
    else:
        response_data['status'] = 'failure'
        response_data['message'] = 'API version does not exist'
        return JsonResponse(response_data)

@csrf_exempt
def addChat(request, version):
    response_data = {}
    if version == 'v1':
        if request.method == "POST":
            c = Chat(doctor_id = request.POST["doctor_id"], patient_id = request.POST["patient_id"], text = request.POST["text"], sender = request.POST["sender"])
            c.save()
            response_data['status'] = "success"
            response_data['data'] = c.id
        else:
            response_data['status'] = "error"
            response_data['message'] = "invalid request"
        return JsonResponse(response_data)
    else:
        response_data['status'] = 'failure'
        response_data['message'] = 'API version does not exist'
        return JsonResponse(response_data)

@csrf_exempt
def getChats(request, version):
    response_data = {}
    if version == 'v1':
        if request.method == "GET":
            if request.GET["user_type"] == "doctor":
                data = Chat.objects.filter(doctor_id = request.GET["id"])
                response_data['status'] = "success"
                response_data['data'] = list(data.values())
                return JsonResponse(response_data)
            elif request.GET["user_type"] == "patient":
                data = Chat.objects.filter(patient_id = request.GET["id"])
                response_data['status'] = "success"
                response_data['data'] = list(data.values())
                return JsonResponse(response_data)
            else:
                response_data = {}
                response_data['status'] = 'failure'
                response_data['message'] = 'invalid type'
                return JsonResponse(response_data)
        else:
            response_data['status'] = "error"
            response_data['message'] = "invalid request"
        return JsonResponse(response_data)
    else:
        response_data['status'] = 'failure'
        response_data['message'] = 'API version does not exist'
        return JsonResponse(response_data)

@csrf_exempt
def addData(request, version):
    response_data = {}
    if version == 'v1':
        if request.method == "POST":
            d = Data(patient_id = request.POST["patient_id"], created = request.POST["created"], ecg_url = request.POST["ecg_url"], temperature = request.POST["temperature"])
            d.save()
            response_data['status'] = "success"
            response_data['data'] = d.id
        else:
            response_data['status'] = "error"
            response_data['message'] = "invalid request"
        return JsonResponse(response_data)
    else:
        response_data['status'] = 'failure'
        response_data['message'] = 'API version does not exist'
        return JsonResponse(response_data)

@csrf_exempt
def getData(request, version):
    response_data = {}
    if version == 'v1':
        if request.method == "GET":
            data = Data.objects.filter(patient_id = request.GET["patient_id"])

            response_data['status'] = "success"
            response_data['data'] = list(data.values())
            return JsonResponse(response_data)
        else:
            response_data['status'] = "error"
            response_data['message'] = "invalid request"
        return JsonResponse(response_data)
    else:
        response_data['status'] = 'failure'
        response_data['message'] = 'API version does not exist'
        return JsonResponse(response_data)

@csrf_exempt
def analyzeECG(request, version):
    response_data = {}
    if version == 'v1':
        if request.method == "GET":
            data = hp.get_data(getECG(request.GET['id']))
            print(data)
            working_data, measures = hp.process(data, 100.0)
            print(measures['bpm'])
            print(measures['rmssd'])
            print(measures)
            hp.plotter(working_data, measures)
            response_data['status'] = "success"
            response_data['message'] = measures
            return JsonResponse(response_data)
        else:
            response_data['status'] = "error"
            response_data['message'] = "invalid request"
            return JsonResponse(response_data)
    else:
        response_data['status'] = 'failure'
        response_data['message'] = 'API version does not exist'
        return JsonResponse(response_data)


def getECG(data_id):
    print(Data.objects.filter(id = data_id))
    dataObject = Data.objects.filter(id = data_id)
    url = dataObject.values('ecg_url')[0]['ecg_url']
    timeStamp = dataObject.values('created')[0]['created']
    patient_id = dataObject.values('patient_id')[0]['patient_id']
    urllib.request.urlretrieve(url,"{}_{}.csv".format(patient_id,timeStamp))
    return ("{}_{}.csv".format(patient_id,timeStamp))
