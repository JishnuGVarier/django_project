from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=50)
    spec=models.CharField(max_length=50)
    number=models.CharField(max_length=10)

'''class Patient(models.Model):
pname=models.CharField(max_length=50)
spec=models.CharField(max_length=100)
number=models.CharField(max_length=50)'''