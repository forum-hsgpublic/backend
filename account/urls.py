from rest_framework.routers import DefaultRouter
from .views import (
    SignupViewSet,
    TokenViewSet,
)

router = DefaultRouter()
router.register(r'auth/signup', SignupViewSet, basename='signup')
router.register(r'auth/token', TokenViewSet, basename='token')
# router.register(r'token/refresh', TokenRefreshView, basename='token-refresh')