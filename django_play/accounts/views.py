from http.client import OK
from django.contrib.auth.models import User, Group
from rest_framework import mixins, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from drf_spectacular.utils import extend_schema

from django_play.accounts.serializers.user import (
    LoginResponseSerializer,
    UserSerializer,
    LoginPayloadSerializer,
)
from django_play.accounts.serializers.group import GroupSerializer


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
        token = payload_serializer.get_user_token()
        response_serializer = LoginResponseSerializer(data={"token": token.key})
        response_serializer.is_valid(raise_exception=True)
        return Response(response_serializer.data, status=OK)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
