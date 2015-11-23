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

from apps.authentication import views as auth_view
from apps.appointment import views as appo_view
from apps.medical import views as medi_view

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Authentication
    url(r'^login/$', auth_view.login, name='login'),
    url(r'^logout/$', auth_view.logout, name='logout'),
    url(r'^reset_password/$', auth_view.reset_password, name='reset_password'),
    url(r'^register/$', auth_view.register, name='register'),
    url(r'^update_profile/$', auth_view.update_profile, name='update_profile'),
    url(r'^change_password/$', auth_view.change_password, name='change_password'),
    url(r'^home/$', auth_view.home, name='home'),
    url(r'^list_patient/', auth_view.list_patient, name='list_patient'),
    url(r'^list_doctor/', auth_view.list_doctor, name='list_doctor'),

    url(r'^list_officer/$', auth_view.list_officer, name='list_officer'),
    url(r'^add_officer/$', auth_view.add_officer, name='add_officer'),
    url(r'^update_officer/$', auth_view.update_officer, name='update_officer'),


    # Appointment
    # url(r'^make_appointment/$', appo_view.make_appointment, name='make_appointment'),
    url(r'^staff_make_appointment/([0-9]+)/$', appo_view.staff_make_appointment, name='staff_make_appointment'),
    url(r'^make_appointment/([0-9]+)/$', appo_view.make_appointment, name='make_appointment'),
    # url(r'^list_appointment/$', appo_view.list_appointment, name='list_appointment'),
    url(r'^list_appointment/([0-9]+)/$', appo_view.list_appointment, name='list_appointment'),
    # url(r'^view_appointment/$', appo_view.view_appointment, name='view_appointment'),
    url(r'^cancel_appointment/([0-9]+)/$', appo_view.cancel_appointment, name='cancel_appointment'),

    # url(r'^make_clinic_time/$', appo_view.make_clinic_time, name='make_clinic_time'),
    url(r'^staff_make_clinic_time/([0-9]+)/$', appo_view.staff_make_clinic_time, name='staff_make_clinic_time'),
    url(r'^make_clinic_time/([0-9]+)/$', appo_view.make_clinic_time, name='make_clinic_time'),
    # url(r'^list_clinic_time/$', appo_view.list_clinic_time, name='list_clinic_time'),
    url(r'^list_clinic_time/([0-9]+)/$', appo_view.list_clinic_time, name='list_clinic_time'),
    # url(r'^view_clinic_time/$', appo_view.view_clinic_time, name='view_clinic_time'),
    url(r'^cancel_clinic_time/([0-9]+)/$', appo_view.cancel_clinic_time, name='cancel_clinic_time'),


    # Medical
    url(r'^add_patient_information/([0-9]+)/', medi_view.add_patient_information, name='add_patient_information'),
    # url(r'^view_patient_information/', medi_view.view_patient_information, name='view_patient_information'),
    url(r'^list_patient_information/([0-9]+)/', medi_view.list_patient_information, name='list_patient_information'),

    url(r'^add_medical_record/([0-9]+)/$', medi_view.add_medical_record, name='add_medical_record'),
    # url(r'^view_medical_record/', medi_view.view_medical_record, name='view_medical_record'),
    url(r'^list_medical_record/([0-9]+)/$', medi_view.list_medical_record, name='list_medical_record'),

    url(r'^add_prescription/([0-9]+)/$', medi_view.add_prescription, name='add_prescription'),
    # url(r'^view_prescription/', medi_view.view_prescription, name='view_prescription'),
    url(r'^list_prescription/([0-9]+)/$', medi_view.list_prescription, name='list_prescription'),
]
