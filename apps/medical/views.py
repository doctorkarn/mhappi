from django.http import *
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib import messages

import json, random

from apps.authenication.models import Patient, Officer
from apps.appointment.models import ClinicTime, Appointment
from apps.medical.models import MedicalRecord, PatientInfo, Prescritpion


def record_patient_info(request):
    if request.POST:
        input = {}
        input['patient_id'] = request.POST['patient_id']
        input['officer_id'] = request.POST['officer_id']
        input['patient_info'] = request.POST['patient_info']

        patient_info = PatientInfo.objects.create(
            patient_id 		= input['patient_id'],
            officer_id 		= input['officer_id'],
            information 	= input['patient_info'],
        )

        messages.success(request, 'Record Patient Information')
        return redirect('/record_patient_info/')

    else:
        patients = Patient.objects.all()
        nurses = Officer.objects.filter(position=3)
        data = {
            'patients' : patients,
            'nurses' : nurses,
        }
        return render(request, 'record_patient_info.html', data)


def view_medical_info(request):
    if request.POST:
        input = {}
        input['patient_id'] = request.POST['patient_id']

        patient_info = PatientInfo.objects.filter(patient_id=input['patient_id'])
        medical_info = MedicalRecord.objects.filter(patient_id=input['patient_id'])
        data = {
            'patient_info' : patient_info,
            'medical_info' : medical_info,
        }
        return render(request, 'view_medical_info.html', data)

    else:
        patient_info = PatientInfo.objects.all()
        medical_info = MedicalRecord.objects.all()

        data = {
            'patient_info' : patient_info,
            'medical_info' : medical_info,
        }
        return render(request, 'view_medical_info.html', data)


def record_medical_info(request):
    if request.POST:
        input = {}
        input['patient_id'] = request.POST['patient_id']
        input['officer_id'] = request.POST['officer_id']
        input['symptom'] = request.POST['symptom']
        input['diagnosis'] = request.POST['diagnosis']
        input['drgcode'] = request.POST['drgcode']

        medical_info = MedicalRecord.objects.create(
            patient_id 	= input['patient_id'],
            officer_id 	= input['officer_id'],
            symptom 	= input['symptom'],
            diagnosis 	= input['diagnosis'],
            drg_code 	= input['drgcode'],
        )

        messages.success(request, 'Record Medical Information')
        return redirect('/record_medical_info/')

    else:
        patients = Patient.objects.all()
        doctors = Officer.objects.filter(position=2)
        data = {
            'patients' : patients,
            'doctors' : doctors,
        }
        return render(request, 'record_medical_info.html', data)


def record_prescription(request):
    if request.POST:
        input = {}
        input['patient_id'] = request.POST['patient_id']
        input['officer_id'] = request.POST['officer_id']
        input['drug_list'] = request.POST['drug_list']

        perscritpion = Prescritpion.objects.create(
            patient_id 	= input['patient_id'],
            officer_id 	= input['officer_id'],
            drug_list 	= input['drug_list'],
        )

        messages.success(request, 'Record Prescritpion')
        return redirect('/record_prescription/')

    else:
        patients = Patient.objects.all()
        doctors = Officer.objects.filter(position=2)
        data = {
            'patients' : patients,
            'doctors' : doctors,
        }
        return render(request, 'record_prescription.html', data)


def view_prescription(request):
    if request.POST:
        input = {}
        input['patient_id'] = request.POST['patient_id']

        perscritpion = Perscritpion.objects.filter(patient_id=input['patient_id'])
        data = {
            'perscritpion' : perscritpion,
        }
        return render(request, 'view_prescription.html', data)

    else:
        perscritpion = Perscritpion.objects.all()
        data = {
            'perscritpion' : perscritpion,
        }
        return render(request, 'view_prescription.html', data)