from django.http import *
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/medical')
    return render(request, 'login.html')

def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/medical')

# @login_required(login_url='/login/')
# def main(request):