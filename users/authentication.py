from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions


class NormalUserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        if not request.user.is_staff:
            raise exceptions.AuthenticationFailed

        return (request.user,request.user.id)

    def authenticate_header(self, request):
        pass
