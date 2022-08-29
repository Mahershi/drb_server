from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from ..managers import CustomUserManager

class UserModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        unique=True,
        max_length=16,
        error_messages={
            'unique': 'Username already exists'
        },
        null=False,
        blank=False
    )

    name = models.CharField(max_length=30, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'


    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def has_module_perms(self, app_label):
        return self.is_superuser

    class Meta:
        db_table = 'crm_app_usermodel'
