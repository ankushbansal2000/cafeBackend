from django.db import models

# Create your models here.

def upload_path(instance,filename):
    return '/'.join(['images',str(instance.name),filename])
class itemdetail(models.Model):
    name=models.CharField(max_length=32)
    price=models.CharField(max_length=32)
    quantity=models.CharField(max_length=32)
  #  image=models.ImageField(upload_to='pics')
    image=models.ImageField(upload_to=upload_path)
    desc=models.CharField(max_length=100)
    
    # @property
    # def cart(self):
    #   return self.objects.all()

