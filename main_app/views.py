from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Patient, Doctor, Chat, Data
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import IntegrityError
import heartpy as hp
import urllib.request
import cv2
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from . import model
from keras.preprocessing import image
import numpy as np
import pandas as pd
import json
import os
import biosppy
import matplotlib.pyplot as plt

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
            patient_id = request.GET.get("patient_id")
            print(patient_id)
            data = Patient.objects.get(id = patient_id)
            response_data['status'] = "success"
            data.__dict__.pop('_state')
            response_data['data'] = data.__dict__
        else:
            response_data['status'] = "error"
            response_data['message'] = "invalid request"
        return JsonResponse(json.dumps(response_data), safe = False)
    else:
        response_data['status'] = 'failure'
        response_data['message'] = 'API version does not exist'
        return JsonResponse(json.dumps(response_data), safe = False)

@csrf_exempt
def getDoctor(request, version):
    response_data = {}
    if version == "v1":
        if request.method == "GET":
            doctor_id = request.GET.get("doctor_id")
            data = Doctor.objects.get(id = doctor_id)
            response_data['status'] = "success"
            data.__dict__.pop('_state')
            response_data['data'] = data.__dict__
        else:
            response_data['status'] = "error"
            response_data['message'] = "invalid request"
        return JsonResponse(json.dumps(response_data), safe = False)
    else:
        response_data['status'] = 'failure'
        response_data['message'] = 'API version does not exist'
        return JsonResponse(json.dumps(response_data), safe = False)

@csrf_exempt
def addPatient(request, version):
    response_data = {}
    if version == 'v1':
        if request.method == "POST":
            p = Patient(first_name = request.POST.get("first_name"), last_name = request.POST.get("last_name"), email = request.POST.get("email"), age = request.POST.get("age"), gender = request.POST.get("gender"), blood_group = request.POST.get("blood_group"), weight = request.POST.get("weight"), height = request.POST.get("height"), diabetes = request.POST.get("diabetes"), smoker = request.POST.get("smoker"), drinker = request.POST.get("drinker"))

            try:
                user = User.objects.create_user(username = request.POST.get("email").split("@")[0], email = request.POST.get("email"), password = request.POST.get("password"), first_name = request.POST.get("first_name"), last_name = request.POST.get("last_name"))
                user.save()
                p.save()

                doctor_id = request.POST.get("doctor")
                doctor = Doctor.objects.get(id = doctor_id)
                if(doctor.pending_requests != ''):
                    doctor.pending_requests = str(doctor.pending_requests) + "," + str(p.id)
                else:
                    doctor.pending_requests = str(p.id)
                doctor.save()

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
            d = Doctor(first_name = request.POST.get("first_name"), last_name = request.POST.get("last_name"), email = request.POST.get("email"), age = request.POST.get("age"), gender = request.POST.get("gender"), experience = request.POST.get("experience"), qualification = request.POST.get("qualification"), address = request.POST.get("address"), number = request.POST.get("number"), fees = request.POST.get("fees"))
            try:
                user = User.objects.create_user(username = request.POST.get("email").split("@")[0], email = request.POST.get("email"), password = request.POST.get("password"), first_name = request.POST.get("first_name"), last_name = request.POST.get("last_name"))
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
def getAllPendingRequests(request, version):
    response_data = {}
    if version == 'v1':
        if request.method == "GET":
            doctor_id = request.GET.get("doctor_id")
            data = Doctor.objects.get(id = doctor_id).pending_requests.split(",")
            patient_list = []
            for patient_id in data:
                patient = Patient.objects.get(id = patient_id)
                patient.__dict__.pop('_state')
                patient_list.append(patient.__dict__)
            response_data['status'] = "success"
            response_data['data'] = patient_list
        else:
            response_data['status'] = "error"
            response_data['message'] = "invalid request"
        print(response_data)
        return JsonResponse(json.dumps(response_data), safe = False)
    else:
        response_data['status'] = 'failure'
        response_data['message'] = 'API version does not exist'
        return JsonResponse(json.dumps(response_data), safe = False)

@csrf_exempt
def acceptRequest(request, version):
    response_data = {}
    if version == 'v1':
        if request.method == "POST":
            doctor_id = request.POST.get("doctor_id")
            doctor= Doctor.objects.get(id = doctor_id)
            pending_requests = doctor.pending_requests.split(',')
            pending_requests.remove(request.POST.get("patient_id"))
            doctor.pending_requests = ','.join(pending_requests)
            if(doctor.patients != ''):
                doctor.patients = str(doctor.patients) + "," + str(request.POST.get("patient_id"))
            else:
                doctor.patients = str(request.POST.get("patient_id"))
            doctor.save()
            patient_id = request.POST.get("patient_id")
            patient = Patient.objects.get(id = patient_id)
            patient.doctor = str(request.POST.get("doctor_id"))
            patient.save()
            response_data['status'] = "success"
            response_data['message'] = "request accepted"
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
def addChat(request, version):
    response_data = {}
    if version == 'v1':
        if request.method == "POST":
            c = Chat(doctor_id = request.POST.get("doctor_id"), patient_id = request.POST.get("patient_id"), text = request.POST.get("text"), sender = request.POST.get("sender"))
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
            if request.GET.get("user_type") == "doctor":
                data = Chat.objects.filter(doctor_id = request.GET.get("id"))
                response_data['status'] = "success"
                response_data['data'] = list(data.values())
                return JsonResponse(response_data)
            elif request.GET.get("user_type") == "patient":
                data = Chat.objects.filter(patient_id = request.GET.get("id"))
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
            d = Data(patient_id = request.POST.get("patient_id"), created = request.POST.get("created"), ecg_url = request.POST.get("ecg_url"), temperature = request.POST.get("temperature"))
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
            data = Data.objects.filter(patient_id = request.GET.get("patient_id"))

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
def checkIfAccepted(request, version):
    response_data = {}
    if version == 'v1':
        if request.method == "GET":
            doctor = Patient.objects.get(id = request.GET.get("patient_id")).doctor
            if(doctor != ''):
                response_data['accepted'] = "yes"
            else:
                response_data['accepted'] = "no"
            response_data['status'] = "success"
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
            path = getECG(request.GET.get('id'))
            data = hp.get_data(path)
            deletefile(path)
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
    # print(Data.objects.filter(id = data_id))
    dataObject = Data.objects.filter(id = data_id)
    url = dataObject.values('ecg_url')[0]['ecg_url']
    timeStamp = dataObject.values('created')[0]['created']
    patient_id = dataObject.values('patient_id')[0]['patient_id']
    urllib.request.urlretrieve(url,"{}_{}.csv".format(patient_id,timeStamp))
    return ("{}_{}.csv".format(patient_id,timeStamp))

def deletefile(path):
	os.remove(path)

@csrf_exempt
def predictArrhythmia(request, version):
    flag = 1
    response_data = {}
    if version == 'v1':
        if request.method == "GET":
            # model = load_model('main_app/ecgScratchEpoch2.hdf5')
            # model._make_predict_function()          # Necessary
            # print('Model loaded. Start serving...')
            output = []

            APC, NORMAL, LBB, PVC, PAB, RBB, VEB = [], [], [], [], [], [], []

            path = getECG(request.GET.get('id'))
            # path = "main_app/arrhythmia.csv"
            output.append(str(path))
            result = {"APC": APC, "Normal": NORMAL, "LBB": LBB, "PAB": PAB, "PVC": PVC, "RBB": RBB, "VEB": VEB}


            indices = []

            kernel = np.ones((4,4),np.uint8)
            csv = pd.read_csv(path)
            deletefile(path)
            csv.columns = [' Sample Value']
            csv_data = csv[' Sample Value']
            data = np.array(csv_data)
            # print(data)
            signals = []
            count = 1
            peaks =  biosppy.signals.ecg.christov_segmenter(signal=data, sampling_rate = 100)[0]
            # print(peaks)
            for i in (peaks[1:-1]):

                diff1 = abs(peaks[count - 1] - i)
                # print(diff1)
                diff2 = abs(peaks[count + 1]- i)
                x = peaks[count - 1] + diff1//2
                y = peaks[count + 1] - diff2//2
                signal = data[x:y]
                signals.append(signal)
                count += 1
                indices.append((x,y))


            for count, i in enumerate(signals):
                fig = plt.figure(frameon=False)
                plt.plot(i)
                plt.xticks([]), plt.yticks([])
                for spine in plt.gca().spines.values():
                    spine.set_visible(False)

                # plt.show()
                filename = 'fig' + '.png'
                fig.savefig(filename)
                im_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
                im_gray = cv2.erode(im_gray,kernel,iterations = 1)
                im_gray = cv2.resize(im_gray, (128, 128), interpolation = cv2.INTER_LANCZOS4)
                cv2.imwrite(filename, im_gray)
                im_gray = cv2.imread(filename)
                pred = model.predict(im_gray.reshape((1, 128, 128, 3)))
                pred_class = pred.argmax(axis=-1)
                if pred_class == 0:
                    APC.append(indices[count])
                elif pred_class == 1:
                    NORMAL.append(indices[count])
                elif pred_class == 2:
                    LBB.append(indices[count])
                elif pred_class == 3:
                    PAB.append(indices[count])
                elif pred_class == 4:
                    PVC.append(indices[count])
                elif pred_class == 5:
                    RBB.append(indices[count])
                elif pred_class == 6:
                    VEB.append(indices[count])



            result = sorted(result.items(), key = lambda y: len(y[1]))[::-1]
            output.append(result)
            data = {}
            data['filename'+ str(flag)] = str(path)
            data['result'+str(flag)] = str(result)

            json_filename = 'data.txt'
            with open(json_filename, 'a+') as outfile:
                json.dump(data, outfile)
                flag+=1




            with open(json_filename, 'r') as file:
                filedata = file.read()
            filedata = filedata.replace('}{', ',')
            with open(json_filename, 'w') as file:
                file.write(filedata)
            os.remove('fig.png')

            response_data['status'] = "success"
            response_data['message'] = str(output)
            return JsonResponse(response_data)
        else:
            response_data['status'] = "error"
            response_data['message'] = "invalid request"
            return JsonResponse(response_data)
    else:
        response_data['status'] = 'failure'
        response_data['message'] = 'API version does not exist'
        return JsonResponse(response_data)
