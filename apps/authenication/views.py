from django.http import *
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

import json
import random

from .models import Patient


def login_user(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
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

def logout_user(request):
    logout(request)
    messages.success(request, 'Logout successful')
    return HttpResponseRedirect('/login')

def register_patient(request):
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
        input['birthdate'] = '2000-01-01 00:00:00'
        input['address'] = request.POST['address']
        input['phone'] = request.POST['phone']
        input['email'] = request.POST['email']

        patient = Patient.objects.create(
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

# @login_required(login_url='/login/')
# def main(request):