import logging
from http.client import BAD_REQUEST, NOT_FOUND
from typing import List, Literal, Optional

from django.http import JsonResponse
from rest_framework.exceptions import ErrorDetail, ValidationError
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exception: Optional[Exception], context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exception, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data["status_code"] = response.status_code

        match exception:
            case ValidationError():
                return _handle_validation_error(exception=exception, response=response)

    return response


def handle_not_found(request, exception):
    data = {"status": 404, "message": "Not Found"}
    return JsonResponse(data=data, status=NOT_FOUND)


def _handle_validation_error(exception: ValidationError, response: Response):
    details: List[ErrorDetail]
    value_that_is_invalid: str
    for value_that_is_invalid, details in exception.detail.items():
        for detail in details:
            code: Literal[
                "required", "blank", "min_length", "max_length", "invalid"
            ] = detail.code

            messages = {
                "required": f"{value_that_is_invalid} is required",
                "blank": f"{value_that_is_invalid} is not allowed to be empty",
                "min_length": f"{value_that_is_invalid} has too few characters",
                "max_length": f"{value_that_is_invalid} has too many character",
                "invalid": f"{value_that_is_invalid} is invalid",
            }

            message = messages.get(code)
            if message is None:
                logging.info(f"unknown validation code; {code}")
                message = f"{value_that_is_invalid} is invalid"

            response.data = {"detail": message, "status_code": BAD_REQUEST}

            return response

    return response
