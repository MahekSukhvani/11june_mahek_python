from django.db import models

# Create your models here.

class signup_data(models.Model):
        fnm=models.CharField(max_length=20)
        email=models.EmailField()
        mob=models.BigIntegerField()
        pas=models.CharField(max_length=10)