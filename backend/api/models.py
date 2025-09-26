from django.db import models

# Create your models here.


class student(models.Model):
    print("model.py---------")
    name=models.CharField(max_length=100,null=True,blank=True)
    surname=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)