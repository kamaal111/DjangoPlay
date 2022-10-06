from http.client import UNAUTHORIZED
from rest_framework.exceptions import APIException


class Unauthorized(APIException):
    status_code = UNAUTHORIZED
    default_detail = "Unauthorized"
    default_code = "unauthorized"
