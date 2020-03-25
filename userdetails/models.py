from django.db import models

# Create your models here.
class UserDetails(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50,primary_key=True)
    user_phno = models.BigIntegerField()
    user_pass = models.CharField(max_length=50)
    def __str__(self):
        return self.user_name
     