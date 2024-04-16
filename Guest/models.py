from django.db import models
from Adminstrator.models import *

class tbl_user(models.Model):
   user_name=models.CharField(max_length=50)
   user_gender=models.CharField(max_length=50)
   user_contact=models.CharField(max_length=50)
   user_email=models.CharField(max_length=50)
   user_password=models.CharField(max_length=50)   
   user_confirmpassword=models.CharField(max_length=50)
   place= models.ForeignKey(tbl_place, on_delete=models.CASCADE) 
   user_address=models.CharField(max_length=50)
   user_photo=models.FileField(upload_to='Assets/UserPhoto/')
   user_status=models.IntegerField(default="0")

class tbl_professor(models.Model):
    professor_name=models.CharField(max_length=50)
    professor_contact=models.CharField(max_length=50)
    professor_email=models.CharField(max_length=50)
    professor_password=models.CharField(max_length=50)   
    professor_address=models.CharField(max_length=50)
    place= models.ForeignKey(tbl_place, on_delete=models.CASCADE) 
    professor_photo=models.FileField(upload_to="Assets/ProfPhoto/")
    professor_proof=models.FileField(upload_to="Assets/ProfProof/")
    professor_status=models.IntegerField(default="0") 

class tbl_officer(models.Model):
    officer_name=models.CharField(max_length=50)
    officer_contact=models.CharField(max_length=50)
    officer_email=models.CharField(max_length=50)
    officer_password=models.CharField(max_length=50)   
    officer_address=models.CharField(max_length=50)
    place= models.ForeignKey(tbl_place, on_delete=models.CASCADE) 
    officer_photo=models.FileField(upload_to="Assets/officerPhoto/")
    officer_proof=models.FileField(upload_to="Assets/officerProof/")
    officer_status=models.IntegerField(default="0")   
       

