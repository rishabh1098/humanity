from django.shortcuts import render
from .models import donardetails
import random
# Create your views here.
def registerasdonar(request):
    if request.method=="POST":
        donarname = request.POST.get('donarname', '')
        number = request.POST.get('number', '')
        age = request.POST.get('age', '')
        city = request.POST.get('city', '')
        gender = request.POST.get('gender', '')
        bloodgroup = request.POST.get('bldgrp', '')
        adharcard = request.POST.get('adhar', '')
        dateofrecovery = request.POST.get('date', '')
        donarid1 = random.randint(1, 100000)
        donarid = str(donarid1)
        print(dateofrecovery)
        booking = donardetails(donarid=donarid, donarname=donarname, number=number, age=age, gender=gender,  city=city, bloodgroup=bloodgroup, adharcard=adharcard,dateofrecovery=dateofrecovery)
        booking.save()
    return render(request, 'donar.html')