from __future__ import annotations

from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import UserNotification


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    phone_number = serializers.CharField(max_length=200)
    password = serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'password',
        )


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)

    class Meta:
        model = get_user_model()
        fields = ('password', 'email')


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    phone_number = serializers.CharField(max_length=200)
    image_name = serializers.CharField(max_length=300)

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'image_name',
            "is_staff",
            "is_active",
            "is_verified"
        )


class EmptySerializer(serializers.Serializer):
    pass
