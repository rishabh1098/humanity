from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class donardetails(models.Model):
    donarid=models.CharField(primary_key=True,max_length=10000000,default="")
    donarname=models.CharField(max_length=50,default="" )
    number=models.CharField(max_length=20)
    age=models.CharField(max_length=20)
    gender=models.CharField(max_length=50)
    city=models.CharField(max_length=10)
    adharcard=models.CharField(max_length=10)
    bloodgroup=models.CharField(max_length=200,default="")
    dateofrecovery = models.CharField(max_length=200,default="")
    def __str__(self):
        return self.donarname + "@" + self.bloodgroup