from django.http import *
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib import messages

import json, random

from apps.authentication.models import Patient, Officer
from apps.appointment.models import ClinicTime, Appointment


def make_appointment(request):
    if request.POST:
        input = {}
        input['patient_id'] = request.POST['patient_id']
        input['clinic_time_id'] = request.POST['clinic_time_id']
        input['appointment_status'] = request.POST['appointment_status']

        appointment = Appointment.objects.create(
            patient_id 			= input['patient_id'],
            clinic_time_id 		= input['clinic_time_id'],
            appointment_status 	= input['appointment_status'],
        )

        messages.success(request, 'Appoint Doctor successful')
        return redirect('/appoint_doctor/')

    else:
        patients = Patient.objects.all()
        clinics = ClinicTime.objects.all()
        data = {
            'patients' : patients,
            'clinics' : clinics,
        }
        return render(request, 'appoint_doctor.html', data)


def list_appointment(request):
    return "Under Construction ....."


def view_appointment(request):
    if request.POST:
        input = {}
        input['patient_id'] = request.POST['patient_id']

        appointments = Appointment.objects.filter(patient_id=input['patient_id'])
        data = {
            'appointments' : appointments,
        }
        return render(request, 'view_appoint.html', data)

    else:
        appointments = Appointment.objects.all()
        data = {
            'appointments' : appointments,
        }
        return render(request, 'view_appoint.html', data)


def cancel_appointment(request):
    if request.POST:
        appointment_id = request.POST['appointment_id']

        appointment = Appointment.objects.filter(pk=appointment_id).update(
            appointment_status  = input['appointment_status'],
        )

        messages.success(request, 'Cancel Appointment successful')
        return redirect('/cancel_appoint/')

    else:
        appointments = Appointment.objects.all()
        data = {
            'appointments' : appointments,
        }
        return render(request, 'cancel_appoint.html', data)


def make_clinic_time(request):
    if request.POST:
        input = {}
        input['officer_id'] = request.POST['officer_id']
        input['clinic_time'] = request.POST['clinic_time']
        input['clinic_status'] = request.POST['clinic_status']

        clinic_time = ClinicTime.objects.create(
            officer_id          = input['officer_id'],
            clinic_datetime     = input['clinic_time'],
            clinic_status       = input['clinic_status'],
        )

        messages.success(request, 'Notify Clinic Time successful')
        return redirect('/notify_clinic_time/')

    else:
        # doctors = Officer.objects.all()
        doctors = Officer.objects.filter(position=2)
        data = {
            'doctors' : doctors
        }
        return render(request, 'notify_clinic_time.html', data)


def list_clinic_time(request):
    return "Under Construction ....."


def view_clinic_time(request):
    return "Under Construction ....."


def cancel_clinic_time(request):
    return "Under Construction ....."