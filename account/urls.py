from django.urls import path

from account.views import UserCreateApiView

urlpatterns = [
    path("register/", UserCreateApiView.as_view(), name="register"),
]

app_name = "account"
