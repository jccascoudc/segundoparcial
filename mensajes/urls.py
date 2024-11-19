from django.urls import path
from .views import home_view, CrearMensaje, MensajesRecibidos, EliminarMensaje

urlpatterns = [
    path('', home_view, name='home'),
    path('enviar/', CrearMensaje.as_view(), name='enviar_mensaje'),
    path('recibidos/', MensajesRecibidos.as_view(), name='mensajes_recibidos'),
    path('eliminar/<int:pk>/<str:tipo>/', EliminarMensaje.as_view(), name='eliminar_mensaje'),
]