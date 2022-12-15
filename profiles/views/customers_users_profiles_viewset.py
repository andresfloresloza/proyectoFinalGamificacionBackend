import random

from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from profiles.models import CustomerUserProfile, Pregunta, PreguntaReto2


class CustomersUsersProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUserProfile
        fields = ('customer_user', 'full_name', 'birthday_date', 'phone_number',
                  'image', 'puntos')


class CustomersUsersProfilesViewSet(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, pk=None):
        if pk:
            command = get_object_or_404(CustomerUserProfile, id=pk)
            command_serializers = CustomersUsersProfilesSerializer(command)
            return Response(command_serializers.data, status=status.HTTP_200_OK)
        else:
            command_list = CustomerUserProfile.objects.all()
            command_serializers = CustomersUsersProfilesSerializer(command_list, many=True)
            return Response(command_serializers.data, status=status.HTTP_200_OK)


class PreguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = (
            '__all__')


class PreguntasViewSet(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, pk=None):
        if pk:
            command = get_object_or_404(Pregunta, id=pk)
            command_serializers = PreguntasSerializer(command)
            return Response(command_serializers.data, status=status.HTTP_200_OK)
        else:
            command_list = Pregunta.objects.all()
            command_serializers = PreguntasSerializer(command_list, many=True)
            aleatorio = random.sample(command_serializers.data, k=10)
            return Response(aleatorio, status=status.HTTP_200_OK)
        """        
        if pk:
            command = get_object_or_404(Pregunta, id=pk)
            command_serializers = PreguntasSerializer(command)
            return Response(command_serializers.data, status=status.HTTP_200_OK)
        else:
            command_list = Pregunta.objects.all()
            command_serializers = PreguntasSerializer(command_list, many=True)
            return Response(command_serializers.data, status=status.HTTP_200_OK)
            """

    def aleatoriosQuizzPrincipal(self, pk=None):
        if pk:
            command = get_object_or_404(Pregunta, id=pk)
            command_serializers = PreguntasSerializer(command)
            return Response(command_serializers.data, status=status.HTTP_200_OK)
        else:
            command_list = Pregunta.objects.all()
            command_serializers = PreguntasSerializer(command_list, many=True)
            aleatorio = random.sample(command_serializers.data, k=10)
            return Response(aleatorio, status=status.HTTP_200_OK)

    def aleatoriosDesafio1(self, pk=None):
        if pk:
            command = get_object_or_404(Pregunta, id=pk)
            command_serializers = PreguntasSerializer(command)
            return Response(command_serializers.data, status=status.HTTP_200_OK)
        else:
            command_list = Pregunta.objects.all()
            command_serializers = PreguntasSerializer(command_list, many=True)
            aleatorio = random.sample(command_serializers.data, k=5)
            return Response(aleatorio, status=status.HTTP_200_OK)


class PreguntasReto2Serializer(serializers.ModelSerializer):
    class Meta:
        model = PreguntaReto2
        fields = (
            '__all__')


class PreguntasReto2ViewSet(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, pk=None):
        if pk:
            command = get_object_or_404(PreguntaReto2, id=pk)
            command_serializers = PreguntasReto2Serializer(command)
            return Response(command_serializers.data, status=status.HTTP_200_OK)
        else:
            command_list = PreguntaReto2.objects.all()
            command_serializers = PreguntasReto2Serializer(command_list, many=True)
            aleatorio = random.sample(command_serializers.data, k=10)
            return Response(aleatorio, status=status.HTTP_200_OK)
    """        
    if pk:
         command = get_object_or_404(PreguntaReto2, id=pk)
         command_serializers = PreguntasReto2Serializer(command)
         return Response(command_serializers.data, status=status.HTTP_200_OK)
     else:
         command_list = PreguntaReto2.objects.all()
         command_serializers = PreguntasReto2Serializer(command_list, many=True)
         return Response(command_serializers.data, status=status.HTTP_200_OK)
         """

    def aleatoriosDesafio2(self, pk=None):
        if pk:
            command = get_object_or_404(PreguntaReto2, id=pk)
            command_serializers = PreguntasReto2Serializer(command)
            return Response(command_serializers.data, status=status.HTTP_200_OK)
        else:
            command_list = PreguntaReto2.objects.all()
            command_serializers = PreguntasReto2Serializer(command_list, many=True)
            aleatorio = random.sample(command_serializers.data, k=10)
            return Response(aleatorio, status=status.HTTP_200_OK)
