from django.db import models

# Create your models here.
class Person(models.Model):
    # id=models.AutoField(primary_key=True)  # Automatically created by Django
    fame=models.CharField(max_length=100,blank=True)
    lname=models.CharField(max_length=100, blank=True)
    age=models.CharField(max_length=3, blank=True)
    email=models.EmailField(max_length=100,blank=True)
    mobile=models.PositiveIntegerField()
    address=models.TextField(blank=True)
    
    def __str__(self):
        return self.fname + ' ' + self.lname