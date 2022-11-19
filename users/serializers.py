from rest_framework import serializers

from users.models import User, Address

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'CPF', 'birth_date', 'email', 'password', 'phone_number', 'address']
        
    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

    #email deve conter @ e terminar com '.com' ou '.br' e ter um length 8
    # password deve conter uma letra maiuscula, uma minuscula, um numero e 8 caracteres
    # data de nascimento deve validar se pessoa tem mais de 18 anos
    # name deve conter pelo menos 3 caracteres
    
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'nickname', 'street', 'house_number', 'zipcode', 'city', 'state']
    
    
    

