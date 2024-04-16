from django.db import models
from Adminstrator.models import *
# Create your models here.

class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)


class tbl_adminregistration(models.Model):
    Adminregistration_name=models.CharField(max_length=50)
    Adminregistration_contact=models.CharField(max_length=50)
    Adminregistration_email=models.CharField(max_length=50)
    Adminregistration_password=models.CharField(max_length=50) 

  

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district = models.ForeignKey(tbl_district, on_delete=models.CASCADE) 

class tbl_reply(models.Model):
    reply_name=models.CharField(max_length=1000)



     