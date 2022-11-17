from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14)
    birth_date = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    #addresses = []
    
class Address(models.Model):
    nickname = models.CharField(max_length=20)
    street = models.CharField(max_length=30)
    house_number = models.IntegerField()
    zipcode = models.CharField(max_length=9)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    
