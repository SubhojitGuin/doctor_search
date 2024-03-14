from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)

    # Specify different related names for groups and user_permissions
    groups = models.ManyToManyField(
        Group, related_name='accounts_user_set', blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission, related_name='accounts_user_set', blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
