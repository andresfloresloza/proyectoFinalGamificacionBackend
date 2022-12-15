from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from firebase_admin import auth
from django.contrib.auth import get_user_model


class AuthenticatedView(APIView):
    #permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.user)
        return Response({'User': "s"})


"""
Creacion de cuenta e inicio de sesion con correo electronico y contraseña
"""


class RegisterUser(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        User = get_user_model()
        user = User.objects.get(uid=request.user.uid)
        firebase_data = auth.get_user(user.uid)

        email = firebase_data.email
        username = email.split('@')[0]

        user.email = email
        user.username = username
        user.save()
        return Response({'message': 'User Registered'})
