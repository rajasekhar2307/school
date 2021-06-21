from django.db import models
from django.shortcuts import render,redirect

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length= 40)
    last_name = models.CharField(max_length= 40)
    father_name = models.CharField(max_length= 40)
    mother_name = models.CharField(max_length= 40)
    student_id = models.IntegerField()
    #date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    phone_number = models.BigIntegerField()
    gender = models.CharField(max_length=1)
    address = models.CharField(max_length=50)

