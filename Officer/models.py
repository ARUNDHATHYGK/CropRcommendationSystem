from django.db import models
from Officer.models import *

class tbl_notification(models.Model):
    notification_date=models.DateField(auto_now_add=True)
    notification_title=models.CharField(max_length=100)
    notification_details=models.CharField(max_length=1000) 
    notification_duedate=models.DateField()
    notification_poster=models.FileField(upload_to='Assets/PosterPhoto/')



