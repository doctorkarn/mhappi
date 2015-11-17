from django.http import *
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib import messages

import json, random

from apps.authentication.models import Patient, Officer
from apps.appointment.models import ClinicTime, Appointment
from apps.medical.models import MedicalRecord, PatientInfo, Prescritpion


def add_patient_information(request):
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


def view_patient_information(request):
    return "Under Construction ....."


def list_patient_information(request):
    return "Under Construction ....."


def add_medical_record(request, pid):
    if request.POST:
        input = {}
        input['patient_id'] = pid
        input['officer_id'] = request.user.id
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
        return redirect('/list_patient/')

    else:
        patient_id = pid
        doctor_id = request.user.id
        data = {
            'patient_id' : patient_id,
            'doctor_id' : doctor_id,
        }
        return render(request, 'record_medical_info.html', data)


def view_medical_record(request):
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


def list_medical_record(request, pid):
    patient_infos = PatientInfo.objects.filter(patient_id=pid)
    medical_infos = MedicalRecord.objects.filter(patient_id=pid)
    data = {
        'patient_infos' : patient_infos,
        'medical_infos' : medical_infos,
    }
    return render(request, 'list_medical_info.html', data)


def add_prescription(request):
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


def list_prescription(request):
    return "Under Construction ....."