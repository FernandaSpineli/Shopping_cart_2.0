from datetime import date

from rest_framework import serializers

from users.models import User, Address, UserAddresses

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'CPF', 'birth_date', 'email', 'password', 'phone_number','user_addresses']
        
    # maximo de 5 endereços por usuario      
      
    def validate(self, attrs):
        name = attrs.get('name', '')
        cpf = attrs.get('CPF', '')
        birth_date = attrs.get('birth_date', '')
        email = attrs.get('email', '')
        password = attrs.get('password', '')
               
        if len(name) < 3:
            raise serializers.ValidationError('Nome precisa conter pelo menos 3 caracteres.')
        
        if len(cpf) < 11:
            raise serializers.ValidationError('CPF precisa conter 11 caracteres, digitar somente números.')
        
        if date.today().year - birth_date.year < 18:
            raise serializers.ValidationError('Idade precisa ser maior que 18.')
        
        if not email.endswith('.com') or len(email) <= 15:
            raise serializers.ValidationError('E-mail inválido.')
        

        if validated_email(email):
            raise serializers.ValidationError('E-mail já em uso.')
        
        if len(password) < 8:
            raise serializers.ValidationError('Senha precisa conter pelo menos 8 caracteres.')

        count = validated_password(password)
        if count < 3:
            raise serializers.ValidationError('Senha precisa conter uma letra maiuscula, uma minuscula e um dos simbolos especiais: @ $ _')
            
        return attrs

def validated_email(user_email):
    users = User.objects.all()
    for user in users:
        if user.email == user_email:
            return True

def validated_password(user_password):
    count = 0
    for p in user_password:
        if (p.islower()): 
            count+=1
        if (p.isupper()): 
            count+=1
        if(p=='@'or p=='$' or p=='_'): 
            count+=1
    return count    
    
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'house_number', 'zipcode', 'city', 'state']

    def validate(self, attrs):
        zipcode = attrs.get('zipcode', '')
        if validated_address_zipcode(zipcode):
            raise serializers.ValidationError('CEP já em uso.')
    
def validated_address_nickname(address_nickname):
    addresses = Address.objects.all()
    for address in addresses:
        if address.nickname == address_nickname:
            return True

def validated_address_zipcode(address_zipcode):
    addresses = Address.objects.all()
    for address in addresses:
        if address.zipcode == address_zipcode:
            return True

class UserAddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddresses
        fields = ['id', 'nickname', 'address']
        
    def validate(self, attrs):
        nickname = attrs.get('nickname', '')
        if validated_address_nickname(nickname):
            raise serializers.ValidationError('Apelido de endereço já em uso.')


    
    
    
    

