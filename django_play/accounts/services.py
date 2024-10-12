from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.authtoken.models import Token

from .exceptions import Unauthorized


class AuthenticationService:
    def __init__(self) -> None: ...

    def authenticated_token(self, token: str):
        try:
            return Token.objects.get(key=token)
        except Token.DoesNotExist as e:
            raise Unauthorized from e

    def get_user_token(self, username: str, password: str):
        user = self.__get_authorized_user(username=username, password=password)
        token, _ = Token.objects.get_or_create(user=user)
        return token

    def __get_authorized_user(self, username: str, password: str):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist as e:
            raise Http404 from e

        if not check_password(password, user.password):
            raise Unauthorized()

        return user
