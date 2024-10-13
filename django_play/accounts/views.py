from django.contrib.auth.models import User
from rest_framework import mixins, viewsets

from .serializers import (
    UserSerializer,
)


class UserViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows users to be created or authenticate.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
