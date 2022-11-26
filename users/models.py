from django.db import models

# Create your models here.

class Address(models.Model):
    owner = models.ForeignKey('User', related_name='addresses', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, blank=True)
    street = models.CharField(max_length=30)
    house_number = models.IntegerField(blank=True)
    zipcode = models.CharField(max_length=9)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    
class User(models.Model):
    name = models.CharField(max_length=200)
    CPF = models.CharField(max_length=14)
    birth_date = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    #address = []
    

