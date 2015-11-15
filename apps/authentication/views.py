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
                auth_login(request, user)
                messages.success(request, 'Login successful')
                return HttpResponseRedirect('/login')
            else:
                messages.warning(request, 'User is banned, please contact admin')
                return HttpResponseRedirect('/login')
        else:
            messages.error(request, 'Username or Password is invalid')
            return HttpResponseRedirect('/login')
    else:
        return render(request, 'login.html')


def logout(request):
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


def update_profile(request):
    return "Under Construction ....."


def register(request):
    user = User.objects.get(id=2)
    user.role = 1
    user.save()


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
        user.role = 1
        user.save()

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
        return render(request, 'register.html')
        # return HttpResponse(json.dumps(input))

    else:
        return render(request, 'register.html')


def add_officer(request):
    if request.POST:
        input = {}
        input['username'] = request.POST['username']
        input['password'] = request.POST['password']
        input['confirm_password'] = request.POST['confirm_password']

        input['hospital_id'] = "MDxxxxx" + str(random.randint(0,9))
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
        	position	= 2,
        )

        messages.success(request, 'Register Officer successful')
        return render(request, 'register_officer.html')
        # return HttpResponse(json.dumps(input))

    else:
        return render(request, 'register_officer.html')


def update_officer(request):
    return "Under Construction ....."


def list_officer(request):
    return "Under Construction ....."