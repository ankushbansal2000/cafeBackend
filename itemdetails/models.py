from django.db import models

# Create your models here.

def upload_path(instance,filename):
    return '/'.join(['images',filename])
class itemdetail(models.Model):
    name=models.CharField(max_length=32)
    price=models.CharField(max_length=32)
    quantity=models.CharField(max_length=32)
    #image=models.ImageField(upload_to='pics')
    image=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)

class image(models.Model):
    image=models.ImageField(upload_to=upload_path)

    

