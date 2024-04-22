from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from account.views import UserCreateApiView

urlpatterns = [
    path("register/", UserCreateApiView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="token"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh")
]

app_name = "account"
