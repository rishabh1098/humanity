from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from django.urls import path
from .import views

urlpatterns=[
    path('',views.registerasdonar,name='registerasdonar'),

]