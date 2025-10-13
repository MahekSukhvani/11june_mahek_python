from django.db import models

# Create your models here.

class userrdata(models.Model):
    fnm=models.CharField(max_length=20)
    lnm=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    cpassword=models.CharField(max_length=20)