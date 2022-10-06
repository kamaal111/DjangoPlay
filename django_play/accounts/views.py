from http.client import OK
from django.contrib.auth.models import User, Group
from rest_framework import mixins, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.authtoken.models import Token
from django.http import Http404


from django_play.accounts.serializers.user import UserSerializer, LoginSerializer
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

    @action(detail=False, methods=["POST"], url_path="login")
    def login(self, request: Request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = serializer.get_user_token()
        return Response({"token": token.key}, status=OK)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
