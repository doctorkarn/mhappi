"""mhappi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.authenication import views as auth_view
from apps.appointment import views as appo_view
from apps.medical import views as medi_view

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', auth_view.login_user, name='login'),
    url(r'^logout/$', auth_view.logout_user, name='logout'),
    url(r'^register/$', auth_view.register_patient, name='register'),
    url(r'^register_officer/$', auth_view.register_officer, name='register_officer'),

    url(r'^appoint_doctor/$', appo_view.appoint_doctor, name='appoint_doctor'),
    url(r'^notify_clinic_time/$', appo_view.notify_clinic_time, name='notify_clinic_time'),
    
    url(r'^record_patient_info/', medi_view.record_patient_info, name='record_patient_info'),
    url(r'^record_medical_info/', medi_view.record_medical_info, name='record_medical_info'),
    url(r'^record_prescription/', medi_view.record_prescription, name='record_prescription'),
    
]
