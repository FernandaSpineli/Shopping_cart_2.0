from rest_framework import serializers

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'CPF', 'birth_date', 'email', 'password', 'phone_number']
        
        