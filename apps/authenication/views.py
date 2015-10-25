from django.http import *
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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
    return render(request, 'login.html')

def logout_user(request):
	logout(request)
	messages.success(request, 'Logout successful')
	return HttpResponseRedirect('/login')

# @login_required(login_url='/login/')
# def main(request):