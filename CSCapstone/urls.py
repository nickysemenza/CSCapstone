"""CSCapstone URL Configuration

Created by Harris Christiansen on 9/18/16.

For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
"""
from django.conf.urls import url
from django.contrib import admin

from CSCapstoneApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.getIndex, name='index'),
    url(r'^table$', views.getTable, name='table'),
    url(r'^form$', views.getForm, name='form'),
]
