from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import TareaSerializer
from .models import Tarea


class TareaAPIView(ListAPIView, 
                   CreateAPIView, 
                   RetrieveAPIView, 
                   UpdateAPIView, 
                   DestroyAPIView):
    serializer_class = TareaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        queryset = Tarea.objects.all()
        id = self.kwargs.get('id')
        id_usuario = self.kwargs.get('id_persona')
        fecha_limite = self.kwargs.get('fecha_limite')

        if id:
            queryset = queryset.filter(id=id)
        if id_usuario:
            queryset = queryset.filter(assigned=id_usuario)
        if fecha_limite:
            queryset = queryset.filter(fecha_limite=fecha_limite)

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
