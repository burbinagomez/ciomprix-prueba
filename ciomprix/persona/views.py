# Create your views here.
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
    )
from .serializers import PersonaSerializer
from .models import Persona

class CrearPersonaAPIView(CreateAPIView):
    serializer_class = PersonaSerializer

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

class EliminarPersonaAPIView(DestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    lookup_field = 'id'