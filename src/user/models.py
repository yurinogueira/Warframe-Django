from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

from user.fields import CPFField


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("E-mail obrigatório")

        email = self.normalize_email(email)
        username = slugify(email)

        user = self.model(email=email, username=username, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields["is_staff"] = True
        extra_fields["is_superuser"] = True
        extra_fields.setdefault("is_active", True)

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    cpf = CPFField(unique=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []

    objects = UserManager()

    class Meta:
        ordering = ("-id",)
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self) -> str:
        return str(self.email)
