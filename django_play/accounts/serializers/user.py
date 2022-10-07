from typing import OrderedDict
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from django.http import Http404
from rest_framework.authtoken.models import Token

from django_play.accounts.exceptions import Unauthorized


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

    def create(self, validated_data: OrderedDict):
        updated_data = validated_data
        raw_password: str = updated_data.pop("password")
        updated_data["password"] = make_password(raw_password)
        return super().create(updated_data)


class LoginPayloadSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        fields = ["username", "password"]

    def get_user_token(self):
        user = self.__get_authorized_user()
        token, _ = Token.objects.get_or_create(user=user)
        return token

    def __get_authorized_user(self):
        try:
            user = User.objects.get(username=self.data["username"])
        except User.DoesNotExist as e:
            raise Http404 from e

        if not check_password(self.data["password"], user.password):
            raise Unauthorized()

        return user


class LoginResponseSerializer(serializers.Serializer):
    token = serializers.CharField()

    class Meta:
        fields = ["token"]
