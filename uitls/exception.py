from rest_framework.views import exception_handler as exc_h
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response


def exception_handler(exc, context):
    response = exc_h(exc, context)

    if response is not None:
        return response

    if isinstance(exc, ObjectDoesNotExist):
        data = {"detail": str(exc)}
        return Response(data)

    return None
