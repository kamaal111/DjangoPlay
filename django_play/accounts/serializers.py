from typing import Any, Dict
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.HyperlinkedModelSerializer):
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

    def create(self, validated_data: Dict[str, Any]):
        updated_data = validated_data
        raw_password: str = updated_data.pop("password")
        updated_data["password"] = make_password(raw_password)
        return super().create(updated_data)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]
