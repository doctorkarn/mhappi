from django.http import *
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist

import json
import random

from apps.authentication.models import Patient, Officer


def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                # login save session
                auth_login(request, user)

                # assign role
                if user.is_superuser:
                    request.session['user_role'] = 'admin'
                    return HttpResponseRedirect('/login')
                else:
                    try:
                        patient = Patient.objects.get(id=user.id)
                        request.session['user_role'] = 'patient'
                        request.session['user_info'] = {
                            'hospital_id' : patient.hospital_id,
                            'national_id' : patient.national_id,
                            'prefix_name' : patient.prefix_name,
                            'first_name' : patient.first_name,
                            'last_name' : patient.last_name,
                            'phone' : patient.phone,
                            'email' : patient.email,
                        }
                        return HttpResponseRedirect('/home')
                    except ObjectDoesNotExist:
                        try:
                            officer = Officer.objects.get(id=user.id)
                            request.session['user_role'] = 'patient'
                            request.session['user_info'] = {
                                'hospital_id' : officer.hospital_id,
                                'national_id' : officer.national_id,
                                'prefix_name' : officer.prefix_name,
                                'first_name' : officer.first_name,
                                'last_name' : officer.last_name,
                                'phone' : officer.phone,
                                'email' : officer.email,
                            }
                            if officer.position == 1:
                                request.session['user_role'] = 'staff'
                                return HttpResponseRedirect('/home')
                            elif officer.position == 2:
                                request.session['user_role'] = 'doctor'
                                return HttpResponseRedirect('/home')
                            elif officer.position == 3:
                                request.session['user_role'] = 'nurse'
                                return HttpResponseRedirect('/home')
                            elif officer.position == 4:
                                request.session['user_role'] = 'pharmacist'
                                return HttpResponseRedirect('/home')
                            else:
                                request.session['user_role'] = 'unknown officer'
                                auth_logout(request)
                                messages.error(request, 'User is invalid, please contact admin')
                                return HttpResponseRedirect('/login')

                        except ObjectDoesNotExist:
                            auth_logout(request)
                            messages.error(request, 'User is invalid, please contact admin')
                            return HttpResponseRedirect('/login')

                # messages.success(request, 'Login successful')
                # return HttpResponseRedirect('/login')
            else:
                messages.warning(request, 'User is banned, please contact admin')
                return HttpResponseRedirect('/login')
        else:
            messages.error(request, 'Username or Password is invalid')
            return HttpResponseRedirect('/login')
    else:
        return render(request, 'login.html')


def logout(request):
    try:
        del request.session['user_role']
    except KeyError:
        pass
    auth_logout(request)
    messages.success(request, 'Logout successful')
    return HttpResponseRedirect('/login')


def reset_password(request):
    if request.POST:
        to_email = request.POST['email']

        # update new password into database
        # .....

        # send new username and password via email
        email_subject = 'Subject here'
        email_message = 'Here is the message.'
        mail_success = send_mail(email_subject, email_message, 'mhappi@karnlab.com', [to_email])

        if mail_success:
            messages.success(request, 'System send new password to your email account, please check your inbox.')
            return HttpResponseRedirect('/login')
        else:
            messages.warning(request, 'System cannot send you an email')
            return HttpResponseRedirect('/login')
        
    else:
        return render(request, 'reset_password.html')


def change_password(request):
    return "Under Construction ....."


def update_profile(request):
    logged_in = request.user.is_authenticated
    uid = request.user.id

    if request.POST:
        input = {}
        input['first_name'] = request.POST['first_name']
        input['last_name'] = request.POST['last_name']

        input['address'] = request.POST['address']
        input['phone'] = request.POST['phone']
        input['email'] = request.POST['email']

        user = User.objects.get(id=request.user.id)
        user.email = input['email']
        user.save()

        patient = Patient.objects.get(id=uid)
        patient.first_name  = input['first_name']
        patient.last_name  = input['last_name']
        patient.address  = input['address']
        patient.phone  = input['phone']
        patient.email  = input['email']
        patient.save()

        messages.success(request, 'Update Profile successful')
        return redirect('/update_profile/')

    else:
        patient = Patient.objects.get(id=uid)
        data = {
            'patient' : patient,
        }
        return render(request, 'update_profile.html', data)


def home(request):
    if request.user.is_authenticated():
        role = request.session.get('user_role')
        if role == 'patient':
            return render(request, 'patient_home.html')
        elif role == 'staff':
            return render(request, 'staff_home.html')
        elif role == 'doctor':
            return render(request, 'doctor_home.html')
        elif role == 'nurse':
            return render(request, 'nurse_home.html')
        elif role == 'pharmacist':
            return render(request, 'pharmacist_home.html')
        else:
            messages.warning(request, 'You have special role, ' + role)
            return HttpResponseRedirect('/login')
    else:
        # messages.warning(request, 'Please login again')
        return HttpResponseRedirect('/login')

def register(request):
    if request.POST:
        input = {}
        input['username'] = request.POST['username']
        input['password'] = request.POST['password']
        input['confirm_password'] = request.POST['confirm_password']

        input['hospital_id'] = "58xxxxx" + str(random.randint(0,9))
        input['national_id'] = request.POST['national_id']
        input['first_name'] = request.POST['first_name']
        input['last_name'] = request.POST['last_name']
        input['gender'] = request.POST['gender']
        input['birthdate'] = '2000-01-01'
        input['address'] = request.POST['address']
        input['phone'] = request.POST['phone']
        input['email'] = request.POST['email']

        user = User.objects.create_user(
            input['username'], input['email'], input['password']
        )

        patient = Patient.objects.create(
        	id 			= user.id,
        	user_id 	= user.id,
        	hospital_id = input['hospital_id'],
        	national_id = input['national_id'],
        	first_name 	= input['first_name'],
        	last_name 	= input['last_name'],
        	gender 		= input['gender'],
        	birthdate 	= input['birthdate'],
        	address 	= input['address'],
        	phone 		= input['phone'],
        	email 		= input['email'],
        )

        messages.success(request, 'Register successful')
        return HttpResponseRedirect('/login')
        # return HttpResponse(json.dumps(input))

    else:
        return render(request, 'register.html')


def list_patient(request):
    patients = Patient.objects.all()
    data = {
        'patients' : patients,
    }
    return render(request, 'list_patient.html', data)


def list_doctor(request):
    doctors = Officer.objects.filter(position=2)
    data = {
        'doctors' : doctors,
    }
    return render(request, 'list_doctor.html', data)


def add_officer(request):
    if request.POST:
        input = {}
        input['username'] = request.POST['username']
        input['password'] = request.POST['password']
        input['confirm_password'] = request.POST['confirm_password']

        input['hospital_id'] = "MDxxxxx" + str(random.randint(0,9)) + str(random.randint(0,9))
        input['national_id'] = request.POST['national_id']
        input['first_name'] = request.POST['first_name']
        input['last_name'] = request.POST['last_name']
        input['gender'] = request.POST['gender']
        input['birthdate'] = '2000-01-01'
        input['address'] = request.POST['address']
        input['phone'] = request.POST['phone']
        input['email'] = request.POST['email']
        input['position'] = request.POST['position']

        user = User.objects.create_user(
            input['username'], input['email'], input['password']
        )
        user.is_staff = 1
        user.save()

        officer = Officer.objects.create(
        	id 			= user.id,
        	user_id 	= user.id,
        	hospital_id = input['hospital_id'],
        	national_id = input['national_id'],
        	first_name 	= input['first_name'],
        	last_name 	= input['last_name'],
        	gender 		= input['gender'],
        	birthdate 	= input['birthdate'],
        	address 	= input['address'],
        	phone 		= input['phone'],
        	email 		= input['email'],
        	position	= input['position'],
        )

        messages.success(request, 'Add Officer successful')
        return redirect('/add_officer/')
        # return HttpResponse(json.dumps(input))

    else:
        return render(request, 'add_officer.html')


def update_officer(request):
    return "Under Construction ....."


def list_officer(request):
    return "Under Construction ....."