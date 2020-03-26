from django.db import models
from itemdetails.models import itemdetail
from userdetails.models import UserDetails 
# Create your models here.

class cartdetail(models.Model):
    emailid = models.CharField(max_length=50)
    item_name=models.CharField(max_length=50)
    item_price=models.CharField(max_length=10)
    quantity = models.CharField(max_length=5)
    
