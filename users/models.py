from __future__ import annotations

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

from user_management import settings


class APIUserManager(BaseUserManager):
    """Custom user manager."""

    use_in_migrations = True

    def create_user(self, validated_data):
        """Create a user."""
        if not validated_data.get('email'):
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(validated_data.get('email')),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            phone_number=validated_data.get('phone_number', ''),
            is_verified=True,
        )

        user.set_password(
            validated_data.get(
                'password', settings.DEFAULT_PASSWORD,
            ),
        )
        user.save()
        return user

    def create_superuser(self, email, password):
        """Create a superuser."""
        super_user_obj = {}
        super_user_obj['email'] = email
        super_user_obj['password'] = password
        super_user_obj['first_name'] = 'Admin'
        user = self.create_user(super_user_obj)
        user.is_staff = True
        user.is_superuser = True
        user.is_verified = True
        user.save()
        return user


class APIUser(AbstractBaseUser, PermissionsMixin):
    """Custom user class."""

    USERNAME_FIELD = 'email'

    USER_TYPE_ADMIN = 'admin'

    # username field not used, only here to make django-rest-auth work
    email = models.EmailField(blank=False, unique=True)
    first_name = models.CharField(
        'first name', max_length=50, null=True, blank=True,
    )
    last_name = models.CharField(
        'last name', max_length=50, null=True, blank=True,
    )
    phone_number = models.CharField(max_length=20, verbose_name='phone number')

    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text='Designates whether this user should be treated as active. '
        'Deselect this instead of deleting accounts.',
    )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    image_name = models.CharField(max_length=300)

    objects = APIUserManager()

    class Meta:
        """Model meta data."""

        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        """Get full name."""
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def get_short_name(self):
        """Get short name."""
        return self.first_name


class Token(models.Model):
    user_id = models.ForeignKey(
        APIUser, blank=True, null=True, on_delete=models.CASCADE,
    )
    refresh_token = models.TextField(blank=True, null=True)
    access_token = models.TextField(blank=True, null=True)
    is_expired = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserNotification(models.Model):
    user_id = models.ForeignKey(
        APIUser, blank=True, null=True, on_delete=models.CASCADE,
    )
    notification_text = models.TextField(blank=True, null=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class LoginLog(models.Model):
    user_id = models.ForeignKey(
        APIUser, blank=True, null=True, on_delete=models.CASCADE,
    )
    login_count = models.IntegerField(null=True, blank=True, default=0)
    last_logged_in = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# models.py
from django.db import models

class CountryPopulation(models.Model):
    place = models.IntegerField(null=True, blank=True)
    pop1980 = models.BigIntegerField(null=True, blank=True)
    pop2000 = models.BigIntegerField(null=True, blank=True)
    pop2010 = models.BigIntegerField(null=True, blank=True)
    pop2022 = models.BigIntegerField(null=True, blank=True)
    pop2023 = models.BigIntegerField(null=True, blank=True)
    pop2030 = models.BigIntegerField(null=True, blank=True)
    pop2050 = models.BigIntegerField(null=True, blank=True)
    country = models.CharField(max_length=200,null=True, blank=True)
    area = models.BigIntegerField(null=True, blank=True)
    landAreaKm = models.FloatField(null=True, blank=True)
    cca2 = models.CharField(max_length=2,null=True, blank=True)
    cca3 = models.CharField(max_length=3,null=True, blank=True)
    netChange = models.FloatField(null=True, blank=True)
    growthRate = models.FloatField(null=True, blank=True)
    worldPercentage = models.FloatField(null=True, blank=True)
    density = models.FloatField(null=True, blank=True)
    densityMi = models.FloatField(null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)
