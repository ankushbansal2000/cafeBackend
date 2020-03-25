from django.db import models

# Create your models here.
class admindetail(models.Model):
    name=models.CharField(max_length=32)
    phoneNo=models.BigIntegerField()
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=15)
    
