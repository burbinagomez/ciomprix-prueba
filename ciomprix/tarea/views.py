# Create your views here.
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
    )
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import TareaSerializer
from .models import Tarea

class CrearTareaAPIView(CreateAPIView):
    serializer_class = TareaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

class ListarTareaAPIView(ListAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class DetalleTareaAPIView(RetrieveAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ActualizarTareaAPIView(UpdateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class EliminarTareaAPIView(DestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class TareasPorUsuario(ListAPIView):
    serializer_class = TareaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        id_usuario = self.kwargs['id_usuario']
        queryset = Tarea.objects.filter(usuario_id=id_usuario)
        return queryset
    
class TareasPorFechaLimite(ListAPIView):
    serializer_class = TareaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        id_usuario = self.kwargs['id_usuario']
        queryset = Tarea.objects.filter(usuario_id=id_usuario)
        return queryset