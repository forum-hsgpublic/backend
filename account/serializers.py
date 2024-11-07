from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id',
            'login_id',
            'email',
            'join_date',
            'last_login',
            'is_superuser',
            'is_active',
            'is_staff'
        ]

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = ['login_id', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            login_id=validated_data['login_id'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class TokenSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField()
    password = serializers.CharField(write_only=True, style={"input_type": "password"})