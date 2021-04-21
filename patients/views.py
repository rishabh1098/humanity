from django.shortcuts import render
from .models import patientdetails
import random
# Create your views here.
def patientregister(request):
    if request.method=="POST":
        patientname = request.POST.get('patientname', '')
        number = request.POST.get('number', '')
        age = request.POST.get('age', '')
        city = request.POST.get('city', '')
        gender = request.POST.get('gender', '')
        bloodgroup = request.POST.get('bldgrp', '')
        hospitalname = request.POST.get('hospital', '')
        casesheet = request.POST.get('casesheet', '')
        patientid1 = random.randint(1, 100000)
        patientid = str(patientid1)
        booking = patientdetails(patientid=patientid, patientname=patientname, number=number, age=age, gender=gender,  city=city, bloodgroup=bloodgroup, hospitalname=hospitalname,doctorcasesheet=casesheet)
        booking.save()
    return render(request, 'patientregister.html')