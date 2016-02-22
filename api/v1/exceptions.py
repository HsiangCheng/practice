# --coding: utf-8--
from rest_framework import status
from rest_framework.exceptions import APIException


class UniqueError(APIException):
    status_code = status.HTTP_200_OK
    default_detail = 'The data is not unique.'
