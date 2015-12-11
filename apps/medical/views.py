from django.http import *
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib import messages

import json, random

from apps.authentication.models import Patient, Officer
from apps.appointment.models import ClinicTime, Appointment
from apps.medical.models import MedicalRecord, PatientInfo, Prescritpion, DrugList, DrgCode


def add_patient_information(request, pid):
    if request.POST:
        input = {}
        input['patient_id'] = pid
        input['officer_id'] = request.user.id
        input['patient_info'] = request.POST['patient_info']

        patient_info = PatientInfo.objects.create(
            patient_id 		= input['patient_id'],
            officer_id 		= input['officer_id'],
            information 	= input['patient_info'],
        )

        messages.success(request, 'Record Patient Information')
        return redirect('/list_patient/')

    else:
        patient_id = pid
        nurse_id = request.user.id
        patient = Patient.objects.filter(id=patient_id)
        data = {
            'patient_id' : patient_id,
            'nurse_id' : nurse_id,
            'patient' : patient
        }
        return render(request, 'record_patient_info.html', data)


def view_patient_information(request):
    return "Under Construction ....."


def list_patient_information(request, pid):
    # patient = Patient.objects.filter(pk=pid)
    patient_infos = PatientInfo.objects.filter(patient_id=pid)
    medical_infos = MedicalRecord.objects.filter(patient_id=pid)
    data = {
        # 'patient' : patient,
        'patient_infos' : patient_infos,
        'medical_infos' : medical_infos,
    }
    return render(request, 'list_patient_info.html', data)


def add_medical_record(request, pid):
    if request.POST:
        input = {}
        input['patient_id'] = pid
        input['officer_id'] = request.user.id
        input['symptom'] = request.POST['symptom']
        input['diagnosis'] = request.POST['diagnosis']
        input['drgcode'] = request.POST['drg_code']
        input['drug_list'] = request.POST['drug_list']

        medical_info = MedicalRecord.objects.create(
            patient_id 	= input['patient_id'],
            officer_id 	= input['officer_id'],
            symptom 	= input['symptom'],
            diagnosis 	= input['diagnosis'],
            drg_code_id 	= input['drgcode'],
        )
        perscritpion = Prescritpion.objects.create(
            patient_id  = input['patient_id'],
            officer_id  = input['officer_id'],
            drug_list   = input['drug_list'],
        )

        messages.success(request, 'Record Medical Information (and Prescritpion) for Patient ID:' + pid)
        return redirect('/list_patient/')

    else:
        patient_id = pid
        patient = Patient.objects.filter(id=pid).first()
        doctor_id = request.user.id
        current_patient_info = PatientInfo.objects.filter(patient_id=pid).order_by('-created_at').first()
        patient_infos  = PatientInfo.objects.filter(patient_id=pid).order_by('-created_at').all()
        medical_infos  = MedicalRecord.objects.filter(patient_id=pid).order_by('-created_at').all()
        prescriptions = Prescritpion.objects.filter(patient_id=pid).order_by('-created_at').all()
        drg_codes = DrgCode.objects.all()
        drug_list = DrugList.objects.all()
        data = {
            'current_patient_info' : current_patient_info,
            'patient_infos' : patient_infos,
            'medical_infos' : medical_infos,
            'prescriptions' : prescriptions,
            'patient_id' : patient_id,
            'doctor_id' : doctor_id,
            'patient' : patient,
            'drg_codes' : drg_codes,
            'drug_list' : drug_list,
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
    patient = Patient.objects.get(id=pid)
    patient_infos = PatientInfo.objects.filter(patient_id=pid)
    medical_infos = MedicalRecord.objects.filter(patient_id=pid)
    prescriptions = Prescritpion.objects.filter(patient_id=pid)
    data = {
        'patient' : patient,
        'patient_infos' : patient_infos,
        'medical_infos' : medical_infos,
        'prescriptions' : prescriptions,
    }
    return render(request, 'list_medical_info.html', data)


def add_prescription(request, pid):
    if request.POST:
        input = {}
        input['patient_id'] = pid
        input['officer_id'] = request.user.id
        input['drug_list'] = request.POST['drug_list']

        perscritpion = Prescritpion.objects.create(
            patient_id 	= input['patient_id'],
            officer_id 	= input['officer_id'],
            drug_list 	= input['drug_list'],
        )

        messages.success(request, 'Record Prescritpion')
        return redirect('/list_patient/')

    else:
        patient_id = pid
        doctor_id = request.user.id
        data = {
            'patient_id' : patient_id,
            'doctor_id' : doctor_id,
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


def list_prescription(request, pid):
    prescriptions = Prescritpion.objects.filter(patient_id=pid)
    patient = Patient.objects.filter(id=pid).first()
    for pres in prescriptions:
        pres.list = pres.drug_list.split(',')
    data = {
        'prescriptions' : prescriptions,
        'patient' : patient
    }
    return render(request, 'list_prescription.html', data)

# def add_drug_list(request):
#     drug_list = DrugList.objects.create(
#         description  = input['patient_id'],
#     )
#     messages.success(request, 'Add All Drug List')
#     return redirect('/login/')