from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(max_length=150, required=True)
    email = serializers.EmailField(min_length=5, required=True)
    password = serializers.CharField(min_length=4, max_length=128, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop("password")
        return representation


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]
