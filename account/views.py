from django.contrib.auth import get_user_model
from rest_framework import generics

from account.serializers import UserSerializer


class UserCreateApiView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
