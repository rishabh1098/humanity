from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class patientdetails(models.Model):
    patientid=models.CharField(primary_key=True,max_length=10000000,default="")
    patientname=models.CharField(max_length=50,default="" )
    number=models.CharField(max_length=20)
    age=models.CharField(max_length=20)
    gender=models.CharField(max_length=50)
    city=models.CharField(max_length=10)
    hospitalname=models.CharField(max_length=10)
    doctorcasesheet=models.CharField(max_length=10)
    bloodgroup=models.CharField(max_length=200,default="")
    dateofregister = models.CharField(max_length=200,default="")
    def __str__(self):
        return self.patientname + "@" + self.bloodgroup