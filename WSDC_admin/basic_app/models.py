from django.db import models

# Create your models here.
class display(models.Model):
    Name=models.CharField(max_length=200)
    Birthdate=models.CharField(max_length=200)
    adhaar=models.IntegerField()
    address=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    specialization=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='photo')
    class Meta:
        db_table="form_info"        

    