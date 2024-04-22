from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

from helpers import upload_image_file_path
from account.managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    bio = models.CharField(max_length=255, blank=True, null=True)
    picture = models.ImageField(
        upload_to=upload_image_file_path,
        blank=True,
        null=True
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f"{self.pk} {self.email}"
