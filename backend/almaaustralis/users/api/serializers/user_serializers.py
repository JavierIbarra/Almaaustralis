from rest_framework import serializers
from users.models import User
import re

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField(write_only=True)

    def create(self, validate_data):
        instance = User()
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance

    def validate_email(self, data):
        users = User.objects.filter(email = data)
        if len(users) != 0:
            raise serializers.ValidationError("Este email ya existe")
        else:
            return data

    def validate_password(self, data):
        print('validate_password')
        if not self.custom_validate_password(data):
            raise serializers.ValidationError({"password": "La contraseña debe tener al menos 10 caracteres, 1 mayúscula, 1 minúscula y 1 carácter especial"})
        else:
            return data

    def custom_validate_password(self, data):
        regexp_password =  r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$'
        pat = re.compile(regexp_password) 
        result = re.search(pat, data) 
        if result:
            return True
        else:
            return False

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Los campos de contraseña no coinciden"})
            
        return attrs