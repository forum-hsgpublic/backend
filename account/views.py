from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import check_password
from .models import User
from .serializers import UserSerializer, SignupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입이 완료되었습니다."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TokenView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        login_id = request.data['login_id']
        password = request.data['password']
        user = User.objects.filter(login_id=login_id).first()
        is_correct_password = check_password(password, user.password)

        if (user is None) or (not is_correct_password):
            return Response({"message: 아이디 또는 비밀번호가 유효하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)
        if user is not None:
            token = TokenObtainPairSerializer.get_token(user)
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