from django.db import models
from jsonfield import JSONField
# Create your models here.

class orderdetail(models.Model):
    email=models.CharField(max_length=50)
    order = JSONField()
