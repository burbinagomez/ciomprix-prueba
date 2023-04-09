# Create your views here.
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
    )
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrAdminOrReadOnly
from .serializers import PersonaSerializer, CreatePersonaSerializer
from .models import Persona

class CrearPersonaAPIView(CreateAPIView):
    serializer_class = CreatePersonaSerializer

class ListarPersonasAPIView(ListAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class DetallePersonaAPIView(RetrieveAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    lookup_field = 'id'

class ActualizarPersonaAPIView(UpdateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdminOrReadOnly]

class EliminarPersonaAPIView(DestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdminOrReadOnly]

class InicioSesion(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(InicioSesion, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key})