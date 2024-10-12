from http.client import CONFLICT, UNAUTHORIZED

from rest_framework.exceptions import APIException


class Unauthorized(APIException):
    status_code = UNAUTHORIZED
    default_detail = "Unauthorized."
    default_code = "unauthorized"


class UserAlreadyExists(APIException):
    status_code = CONFLICT
    default_detail = "User already exists."
    default_code = "user_conflict"
