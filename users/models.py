from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    # Add your custom fields here (e.g., tier relationship)
    tier = models.ForeignKey(
        'tiers.Tier', 
        on_delete=models.CASCADE, 
        related_name='users', 
        null=True, blank=True
    )

    # Avoid conflicts by defining explicit related_name for groups and permissions
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
