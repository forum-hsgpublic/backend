from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    SignupView,
    TokenView,
)

urlpatterns = [
    path('signup', SignupView.as_view(), name='signup'),
    path('token', TokenView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]