from django.http import *
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib import messages
from django.utils import timezone

import json, random, datetime

from apps.authentication.models import Patient, Officer, Department
from apps.appointment.models import ClinicTime, Appointment
from django.core.exceptions import ObjectDoesNotExist


def make_appointment(request, pid):
    if request.POST.get('clinic_time_id'):
        input = {}
        input['patient_id'] = pid
        input['clinic_time_id'] = request.POST['clinic_time_id']
        input['appointment_status'] = 1

        clinic_time = ClinicTime.objects.get(id=input['clinic_time_id'])

        if clinic_time.clinic_status >= 15:
            messages.error(request, 'This Clinic Time is full, please select new clinic time')
            return redirect('/list_appointment/' + pid + '/')

        appointment = Appointment.objects.create(
            patient_id          = input['patient_id'],
            clinic_time_id      = input['clinic_time_id'],
            appointment_status  = input['appointment_status'],
        )
        clinic_time = ClinicTime.objects.get(id=input['clinic_time_id'])
        clinic_time.clinic_status += 1
        clinic_time.save()

        messages.success(request, 'Appoint Doctor successful')
        return redirect('/list_appointment/' + pid + '/')

    elif request.POST.get('doctor_id'):
        did = request.POST['doctor_id']
        clinics = ClinicTime.objects.filter(officer_id=did)
        data = {
            'patient_id' : pid,
            'clinics' : clinics,
        }
        return render(request, 'appoint_doctor.html', data)

    elif request.POST.get('department_id'):
        did = request.POST['department_id']
        clinics = ClinicTime.objects.filter(officer__specialist_id=did)
        data = {
            'patient_id' : pid,
            'clinics' : clinics,
        }
        return render(request, 'appoint_doctor.html', data)

    else:
        doctors = Officer.objects.filter(position=2)
        departments = Department.objects.all()
        data = {
            'patient_id' : pid,
            'doctors' : doctors,
            'departments' : departments,
        }
        return render(request, 'search_doctor.html', data)


def list_appointment(request, pid):
    start = timezone.now() - datetime.timedelta(days=1)
    appointments = Appointment.objects.filter(patient_id=pid, appointment_status=1, clinic_time__clinic_datetime__gte=start).order_by('clinic_time__clinic_datetime')
    patient = Patient.objects.get(id=pid)
    data = {
        'appointments' : appointments,
        'patient_id' : pid,
        'patient' : patient,
    }
    return render(request, 'list_appointment.html', data)


# def view_appointment(request):
#     if request.POST:
#         input = {}
#         input['patient_id'] = request.POST['patient_id']
#         appointments = Appointment.objects.filter(patient_id=input['patient_id'])
#         data = {
#             'appointments' : appointments,
#         }
#         return render(request, 'view_appoint.html', data)

#     else:
#         appointments = Appointment.objects.all()
#         data = {
#             'appointments' : appointments,
#         }
#         return render(request, 'view_appoint.html', data)


# def cancel_appointment(request, pid):
#     if request.POST:
#         appointment_id = request.POST['appointment_id']
#         appointment = Appointment.objects.filter(pk=appointment_id).update(
#             appointment_status  = -1,
#         )
#         clinic_time = ClinicTime.objects.get(id=input['clinic_time_id'])
#         clinic_time.clinic_status -= 1
#         clinic_time.save()

#         messages.success(request, 'Cancel Appointment successful')
#         return redirect('/list_appointment/' + pid + '/')

#     else:
#         appointments = Appointment.objects.filter(patient_id=pid, appointment_status=1)
#         data = {
#             'appointments' : appointments,
#             'patient_id' : pid,
#         }
#         return render(request, 'cancel_appoint.html', data)


def cancel_appointment(request, pid, aid):
    appointment_id = aid
    try:
        appointment = Appointment.objects.get(pk=appointment_id)
        appointment.appointment_status = -1
        appointment.save()
        clinic_time = ClinicTime.objects.get(id=appointment.clinic_time_id)
        clinic_time.clinic_status -= 1
        clinic_time.save()
    except ObjectDoesNotExist:
        messages.success(request, 'Cannot Cancel Appointment')
        return redirect('/list_appointment/' + pid + '/')

    messages.success(request, 'Cancel Appointment successful')
    return redirect('/list_appointment/' + pid + '/')


def make_clinic_time(request, did):
    if request.POST:
        input = {}
        input['officer_id'] = did
        input['clinic_time'] = request.POST['clinic_time']
        input['clinic_status'] = 0

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
    start = timezone.now() - datetime.timedelta(days=1)
    clinic_times = ClinicTime.objects.filter(officer_id=did, clinic_status__gte=0, clinic_datetime__gte=start).order_by('clinic_datetime')
    for clinic in clinic_times:
        clinic.clinic_bar = clinic.clinic_status / 15 * 100
        clinic.save()
    doctor = Officer.objects.get(id=did)
    data = {
        'clinic_times' : clinic_times,
        'doctor_id' : did,
        'doctor' : doctor,
    }
    return render(request, 'list_clinic_time.html', data)


# def cancel_clinic_time(request, did):
#     if request.POST:
#         input = {}
#         input['clinic_time'] = request.POST['clinic_time']

#         clinic_time = ClinicTime.objects.get(id=input['clinic_time_id'])
#         clinic_time.clinic_status = -1
#         clinic_time.save()

#         appointments = Appointment.objects.filter(id=input['clinic_time_id'])
#         for appoint in appointments:
#             appoint.appointment_status = -1
#             appoint.save()

#     else:
#         return redirect('/list_clinic_time/' + did + '/')


def cancel_clinic_time(request, did, cid):
    try:
        clinic_time = ClinicTime.objects.get(id=cid)
        clinic_time.clinic_status = -1
        clinic_time.save()

        appointments = Appointment.objects.filter(clinic_time_id=cid)
        for appoint in appointments:
            appoint.appointment_status = -1
            appoint.save()

    except ObjectDoesNotExist:
        messages.success(request, 'Cannot Cancel Clinic Time')
        return redirect('/list_clinic_time/' + did + '/')

    messages.success(request, 'Cancel Appointment successful')
    return redirect('/list_clinic_time/' + did + '/')


def view_clinic_time(request):
    return "Under Construction ....."
