from django.db import models

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=30)
    house_number = models.IntegerField(blank=True)
    zipcode = models.CharField(max_length=9)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    
class UserAddresses(models.Model):
    nickname = models.CharField(max_length=20, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)    
    user_address = {nickname : address}
    addresses = [user_address]
    
class User(models.Model):
    name = models.CharField(max_length=200)
    CPF = models.CharField(max_length=14)
    birth_date = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    addresses = models.ForeignKey(UserAddresses, on_delete=models.SET_NULL, null=True)
    user_addresses = [addresses]
    

