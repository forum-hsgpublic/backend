from rest_framework import viewsets, status, decorators
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import tokens
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer, SignupSerializer, TokenSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SignupView(APIView):
    @decorators.permission_classes([])
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        if user is not None:
            return Response({"message": "회원가입이 완료되었습니다."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TokenView(APIView):
    @decorators.permission_classes([])
    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        login_id = serializer.validated_data['login_id']
        password = serializer.validated_data['password']
        user = authenticate(login_id=login_id, password=password)

        if user is not None:
            token = tokens.RefreshToken(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            response = Response(
                {
                    "message": "Login succeeded",
                    "user": UserSerializer(user).data,
                    "token": {
                        "access_token": access_token,
                        "refresh_token": refresh_token
                    }
                },
                status=status.HTTP_200_OK
            )
            response.set_cookie("access_token", access_token, httponly=True)
            response.set_cookie("refresh_token", refresh_token, httponly=True)
            return response
        return Response({"message: 아이디 또는 비밀번호가 유효하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)
    
    @decorators.permission_classes([IsAuthenticated])
    def delete(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        token = tokens.RefreshToken(refresh_token)
        token.blacklist()

        response = Response()
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return response