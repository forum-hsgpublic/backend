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
        fields = ['login_id', 'email', 'password', 'password2']

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({"password": "비밀번호가 일치하지 않습니다."})

        user = User(
            login_id=self.validated_data['login_id'],
            email=self.validated_data['email'],
        )
        user.set_password(password)
        user.save()
        return user
    
class TokenSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField()
    password = serializers.CharField(write_only=True, style={"input_type": "password"})