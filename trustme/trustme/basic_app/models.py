from unicodedata import category
from django.db import models

# Create your models here.
class registration(models.Model):
    name=models.CharField(max_length=200)
    birthdate=models.DateField()
    aadhar=models.PositiveBigIntegerField()
    address=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    specialization=models.CharField(max_length=200)
    category=models.FileField()