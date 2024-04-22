from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from account.views import UserCreateApiView

urlpatterns = [
    path("register/", UserCreateApiView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
]

app_name = "account"
