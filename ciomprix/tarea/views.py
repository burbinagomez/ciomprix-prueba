# Create your views here.
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
    )
from .serializers import TareaSerializer
from .models import Tarea

class CrearTareaAPIView(CreateAPIView):
    serializer_class = TareaSerializer

class ListarTareaAPIView(ListAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class DetalleTareaAPIView(RetrieveAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    lookup_field = 'id'

class ActualizarTareaAPIView(UpdateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    lookup_field = 'id'

class EliminarTareaAPIView(DestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    lookup_field = 'id'

class TareasPorUsuario(ListAPIView):
    serializer_class = TareaSerializer

    def get_queryset(self):
        id_usuario = self.kwargs['id_usuario']
        queryset = Tarea.objects.filter(usuario_id=id_usuario)
        return queryset
    
class TareasPorFechaLimite(ListAPIView):
    serializer_class = TareaSerializer

    def get_queryset(self):
        id_usuario = self.kwargs['id_usuario']
        queryset = Tarea.objects.filter(usuario_id=id_usuario)
        return queryset