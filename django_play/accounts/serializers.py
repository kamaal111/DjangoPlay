from typing import OrderedDict

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from .exceptions import UserAlreadyExists


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150, required=True)
    email = serializers.EmailField(min_length=5, required=True)
    password = serializers.CharField(min_length=4, max_length=128, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def to_representation(self, instance: User):
        representation = super().to_representation(instance)
        representation.pop("password")
        return representation

    def create(self, validated_data: OrderedDict):
        updated_data = validated_data

        try:
            User.objects.get(username=updated_data["username"])
        except User.DoesNotExist:
            pass
        else:
            raise UserAlreadyExists

        raw_password: str = updated_data.pop("password")
        updated_data["password"] = make_password(raw_password)
        return super().create(updated_data)


class LoginPayloadSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        fields = ["username", "password"]


class LoginResponseSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)

    class Meta:
        fields = ["token"]
