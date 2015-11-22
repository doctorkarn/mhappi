from django.http import *
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib import messages

import json, random

from apps.authentication.models import Patient, Officer
from apps.appointment.models import ClinicTime, Appointment


def make_appointment(request, pid):
    if request.POST['clinic_time_id']:
        input = {}
        input['patient_id'] = pid
        input['clinic_time_id'] = request.POST['clinic_time_id']
        input['appointment_status'] = 1

        appointment = Appointment.objects.create(
            patient_id 			= input['patient_id'],
            clinic_time_id 		= input['clinic_time_id'],
            appointment_status 	= input['appointment_status'],
        )

        messages.success(request, 'Appoint Doctor successful')
        return redirect('/make_appointment/' + pid + '/')

    elif request.POST['doctor_id']:

        return render(request, 'appoint_doctor.html', data)

    elif request.POST['department_id']:

        return render(request, 'appoint_doctor.html', data)

    else:
        # patients = Patient.objects.all()
        # clinics = ClinicTime.objects.all()
        # data = {
        #     'patients' : patients,
        #     'clinics' : clinics,
        #     'patient_id' : pid,
        # }
        return render(request, 'search_doctor.html', data)


def list_appointment(request, pid):
    appointments = Appointment.objects.filter(patient_id=pid)
    data = {
        'appointments' : appointments,
        'patient_id' : pid,
    }
    return render(request, 'list_appointment.html', data)


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


def make_clinic_time(request, did):
    if request.POST:
        input = {}
        input['officer_id'] = did
        input['clinic_time'] = request.POST['clinic_time']
        input['clinic_status'] = 1

        clinic_time = ClinicTime.objects.create(
            officer_id          = input['officer_id'],
            clinic_datetime     = input['clinic_time'],
            clinic_status       = input['clinic_status'],
        )

        messages.success(request, 'Make Clinic Time successful')
        return redirect('/make_clinic_time/' + did + '/')

    else:
        # doctors = Officer.objects.all()
        doctors = Officer.objects.filter(position=2)
        clinic_times = ClinicTime.objects.filter(officer_id=did) #marrtan edit
        data = {
            'doctors' : doctors,
            'doctor_id' : did,
            'clinic_times' : clinic_times
        }
        return render(request, 'notify_clinic_time.html', data)


def list_clinic_time(request, did):
    clinic_times = ClinicTime.objects.filter(officer_id=did)
    data = {
        'clinic_times' : clinic_times,
        'doctor_id' : did,
    }
    return render(request, 'list_clinic_time.html', data)


def view_clinic_time(request):
    return "Under Construction ....."


def cancel_clinic_time(request):
    return "Under Construction ....."