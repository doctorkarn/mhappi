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
from apps.medical import views as med_view

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_view.login_user, name='login'),
    url(r'^logout/$', auth_view.logout_user, name='logout'),
    
	url(r'^medical/', med_view.index, name='index'),
    
]
