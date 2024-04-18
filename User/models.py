from django.db import models
from Guest.models import *
from Officer.models import *

class tbl_request(models.Model):
    request_date=models.DateField(auto_now_add=True)
    request_title=models.CharField(max_length=100)
    request_details=models.CharField(max_length=1000) 
    request_reply=models.CharField(max_length=1000)
    request_status=models.IntegerField(default="0") 
    user= models.ForeignKey(tbl_user, on_delete=models.CASCADE) 
    professor= models.ForeignKey(tbl_professor, on_delete=models.CASCADE) 


class tbl_apply(models.Model):
    apply_date=models.DateField(auto_now_add=True)
    apply_status=models.IntegerField(default="0") 
    user= models.ForeignKey(tbl_user, on_delete=models.CASCADE) 
    notification= models.ForeignKey(tbl_notification, on_delete=models.CASCADE)


class tbl_complaint(models.Model):
    complaint_date=models.DateField(auto_now_add=True)
    complaint_title=models.CharField(max_length=100)
    complaint_details=models.CharField(max_length=1000)
    complaint_reply=models.CharField(max_length=1000)
    complaint_staus=models.IntegerField(default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)

class tbl_feedback(models.Model):
    feedback_title=models.CharField(max_length=100)
    feedback_date=models.DateField(auto_now_add=True)
    feedback_details=models.CharField(max_length=1000)    




class tbl_predictionHead(models.Model):
    Nitrogen=models.FloatField(max_length=100)
    Phosphorus=models.FloatField(max_length=100)
    Potassium=models.FloatField(max_length=100)
    Temprature=models.FloatField(max_length=100)
    Humidity=models.FloatField(max_length=100)
    Ph=models.FloatField(max_length=100)
    Rainfall=models.FloatField(max_length=100)
    Rainfall=models.FloatField(max_length=100)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)



class tbl_predictionData(models.Model):
    predictionHead = models.ForeignKey(tbl_predictionHead, on_delete=models.CASCADE)
    prediction_result=models.CharField(max_length=100,null=True)
