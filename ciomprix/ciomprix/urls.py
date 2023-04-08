"""
URL configuration for ciomprix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from persona import views as persona_views
from tarea import views as tarea_views

urlpatterns = [
    path("admin/", admin.site.urls),
    #Persona
    path('login/', persona_views.InicioSesion.as_view(), name='inicio-sesion'),
    path('personas/', persona_views.ListarPersonasAPIView.as_view(), name='persona-list'),
    path('personas/<int:id>/', persona_views.DetallePersonaAPIView.as_view(), name='persona-detail'),
    path('personas/create', persona_views.CrearPersonaAPIView.as_view(), name='persona-created'),
    path('personas/<int:id>/update', persona_views.ActualizarPersonaAPIView.as_view(), name='persona-update'),
    path('personas/<int:id>/delete', persona_views.EliminarPersonaAPIView.as_view(), name='persona-delete'),
    #Tareas
    path('tareas/', tarea_views.ListarTareaAPIView.as_view(), name='tarea-list'),
    path('tareas/<int:id>/', tarea_views.DetalleTareaAPIView.as_view(), name='tarea-detail'),
    path('tareas/create', tarea_views.CrearTareaAPIView.as_view(), name='tarea-created'),
    path('tareas/<int:id>/update', tarea_views.ActualizarTareaAPIView.as_view(), name='tarea-update'),
    path('tareas/<int:id>/delete', tarea_views.EliminarTareaAPIView.as_view(), name='tarea-delete'),
]
