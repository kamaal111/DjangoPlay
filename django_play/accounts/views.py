from http.client import OK
from django.contrib.auth.models import User
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from drf_spectacular.utils import extend_schema

from .serializers import (
    LoginResponseSerializer,
    UserSerializer,
    LoginPayloadSerializer,
)
from .services import AuthenticationService


class UserViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer

    @extend_schema(
        request=LoginPayloadSerializer, responses={200: LoginResponseSerializer}
    )
    @action(detail=False, methods=["POST"], url_path="login")
    def login(self, request: Request):
        payload_serializer = LoginPayloadSerializer(data=request.data)
        payload_serializer.is_valid(raise_exception=True)
        validated_data = payload_serializer.data

        authentication_service = AuthenticationService()
        token = authentication_service.get_user_token(
            username=validated_data["username"], password=validated_data["password"]
        )

        response_serializer = LoginResponseSerializer(data={"token": token.key})
        response_serializer.is_valid(raise_exception=True)
        return Response(response_serializer.data, status=OK)
