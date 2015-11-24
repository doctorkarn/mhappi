from django.http import *
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

import json, random, string

from apps.authentication.models import Patient, Officer, Department


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
                        messages.success(request, 'Welcome, ' + user.username)
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
                                request.session['user_dept'] = officer.specialist.name
                                request.session['user_role'] = 'doctor'
                                return HttpResponseRedirect('/home')
                            elif officer.position == 3:
                                request.session['user_dept'] = officer.specialist.name
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
    elif request.user.is_authenticated():
        return HttpResponseRedirect('/home')
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
    logged_in = request.user.is_authenticated
    uid = request.user.id

    if request.POST:
        input = {}
        input['old_password'] = request.POST['old_password']
        input['new_password'] = request.POST['new_password']
        input['confirm_password'] = request.POST['confirm_password']

        user = User.objects.get(id=uid)
        
        if( check_password(input['old_password'], user.password) == False ):
            messages.error(request, 'Old Password is incorrect')
            return HttpResponseRedirect('/change_password/')
        elif( input['new_password'] != input['confirm_password'] ):
            messages.error(request, 'Confirm Password is mismatch')
            return HttpResponseRedirect('/change_password/')
        else:
            user.set_password(input['new_password'])
            user.save()
            messages.success(request, 'Change Password Successfully, Please Login Again.')
            return HttpResponseRedirect('/login/')
            
    else:
        user = User.objects.get(id=uid)
        data = {
            'user' : user,
        }
        return render(request, 'change_password.html', data)


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

        user = User.objects.get(id=uid)
        user.email = input['email']
        user.save()

        try:
            profile = Patient.objects.get(id=uid)
        except ObjectDoesNotExist:
            profile = Officer.objects.get(id=uid)

        profile.first_name  = input['first_name']
        profile.last_name  = input['last_name']
        profile.address  = input['address']
        profile.phone  = input['phone']
        profile.email  = input['email']
        profile.save()

        messages.success(request, 'Update Profile successful')
        return redirect('/home/')

    else:
        user = User.objects.get(id=uid)
        try:
            profile = Patient.objects.get(id=uid)
        except ObjectDoesNotExist:
            profile = Officer.objects.get(id=uid)
        data = {
            'user' : user,
            'profile' : profile,
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
        messages.warning(request, 'Please Login')
        return HttpResponseRedirect('/login')

def register(request):
    if request.POST:
        input = {}
        input['national_id'] = request.POST['national_id']
        input['username'] = input['national_id']
        input['password'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        input['email'] = request.POST['email']
        input['phone'] = request.POST['phone']

        user = User.objects.create_user(
            input['username'], input['email'], input['password']
        )

        if user.id < 10:
            user.digit_id = "00000" + str(user.id)
        elif user.id < 100:
            user.digit_id = "0000" + str(user.id)
        elif user.id < 1000:
            user.digit_id = "000" + str(user.id)
        elif user.id < 10000:
            user.digit_id = "00" + str(user.id)
        elif user.id < 100000:
            user.digit_id = "0" + str(user.id)
        else:
            user.digit_id = str(user.id)

        input['hospital_id'] = str((timezone.now().year+543)%100) + user.digit_id + str(random.randint(0,9)) + str(random.randint(0,9))
        
        user.username = input['hospital_id']
        user.save()

        input['prefix_name'] = request.POST['prefix_name']
        input['first_name'] = request.POST['first_name']
        input['last_name'] = request.POST['last_name']
        input['gender'] = request.POST['gender']

        input['day'] = request.POST['day']
        input['month'] = request.POST['month']
        input['year'] = request.POST['year']
        if( int(input['day']) < 10 ):
            input['day'] = '0' + str(input['day'])
        if( int(input['month']) < 10 ):
            input['month'] = '0' + str(input['month'])

        input['home_id'] = request.POST['home_id']
        input['road'] = request.POST['road']
        input['tambol'] = request.POST['tambol']
        input['amphur'] = request.POST['amphur']
        input['province'] = request.POST['province']
        input['postcode'] = request.POST['postcode']
        

        patient = Patient.objects.create(
        	id 			= user.id,
        	user_id 	= user.id,
        	hospital_id = input['hospital_id'],
        	national_id = input['national_id'],
        	first_name 	= input['first_name'],
        	last_name 	= input['last_name'],
        	gender 		= input['gender'],
        	birthdate 	= input['year'] + '-' + input['month'] + '-' + input['day'],
        	address 	= input['home_id'] + ' ' + input['road'] + ' ' + input['tambol'] + ' ' + input['amphur'] + ' ' + input['province'] + ' ' + input['postcode'],
        	phone 		= input['phone'],
        	email 		= input['email'],
        )

        to_email = input['email']
        email_subject = 'ยืนยันการลงทะเบียนผู้ป่วยระบบ MHAPPI '
        email_message = "เรียน คุณ" + input['first_name'] + " " + input['last_name'] + "\n"
        email_message += "ท่านได้ทำการลงทะเียนผู้ป่วยระบบ MHAPPI \n โดยมีข้อมูลการเข้าสู่ระบบ ดังต่อไปนี้ : \n\n"
        email_message += "username : " + input['username'] + "\n"
        email_message += "password : " + input['password'] + "\n\n"
        email_message += "โดยท่าสามารถเข้าใช้งานระบบของเราได้ที่ {{ URL }} \n"
        email_message += "ขอบคุณที่ใช้บริการของเราค่ะ MHAPPI "
        mail_success = send_mail(email_subject, email_message, 'mhappi@karnlab.com', [to_email])

        # messages.success(request, 'Register successful')
        # return HttpResponseRedirect('/login')
        return render(request, 'success.html')

    else:
        data = {
            'day_range' : range(1,32),
            'month_range' : range(1,13),
            'year_range' : range(1900,timezone.now().year),
        }
        return render(request, 'register.html', data)


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


def handle_uploaded_file(f, i):
    with open('static/avatar/'+str(i)+'.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def add_officer(request):
    if request.POST:
        input = {}
        input['username'] = request.POST['username']
        input['password'] = request.POST['password']
        input['confirm_password'] = request.POST['confirm_password']

        if user.id < 10:
            user.digit_id = "00000" + user.id
        if user.id < 100:
            user.digit_id = "0000" + user.id
        if user.id < 1000:
            user.digit_id = "000" + user.id
        if user.id < 10000:
            user.digit_id = "00" + user.id
        if user.id < 100000:
            user.digit_id = "0" + user.id

        input['hospital_id'] = "MD" + user.digit_id + str(random.randint(0,9)) + str(random.randint(0,9))
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

        handle_uploaded_file(request.FILES['picture'], user.id)

        messages.success(request, 'Add Officer successful')
        return redirect('/add_officer/')
        # return HttpResponse(json.dumps(input))

    else:
        departments = Department.objects.all()
        data = {
            'departments': departments,
        }
        return render(request, 'add_officer.html', data)


def update_officer(request):
    return "Under Construction ....."


def list_officer(request):
    return "Under Construction ....."