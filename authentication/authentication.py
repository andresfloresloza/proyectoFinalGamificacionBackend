import os
from time import sleep

import firebase_admin
from django.contrib.auth import get_user_model
from django.utils import timezone
from firebase_admin import auth, credentials
from rest_framework.authentication import BaseAuthentication
from .exceptions import FirebaseAuthException, InvalidToken, TokenNotFound, EmailNotVerified

cred = credentials.Certificate(os.path.join(
    os.path.dirname(__file__), 'secrets/firebaseconfig.json'))

app = firebase_admin.initialize_app(cred)


class FirebaseAuthentication(BaseAuthentication):
    """
    Acceso a datos solo si se inicio sesion en firebase
    """

    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            print(TokenNotFound())
            raise TokenNotFound()

        token = auth_header.split(' ').pop()
        sleep(2)

        try:
            decoded_token = auth.verify_id_token(token)
        except Exception as e:
            raise InvalidToken()
        try:
            uid = decoded_token.get('uid')
            user = auth.get_user(uid, app)
        except Exception as e:
            raise FirebaseAuthException()

        User = get_user_model()

        try:
            objUser = User.objects.filter(uid=user.uid)
            if objUser and not user.email_verified:
                raise EmailNotVerified()
        except Exception as e:
            raise EmailNotVerified()
        try:
            user, created = User.objects.get_or_create(uid=uid)
            pass
        except Exception as e:
            print('this is problem', e)
            return None
        return user, None
