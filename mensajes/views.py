from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from mensajes.models import Mensaje
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

class RegistroUsuario(CreateView):
    template_name = 'registration/registro.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


def home_view(request):
    return render(request,'home.html')

class CrearMensaje(CreateView):
    model = Mensaje
    fields = ['destinatario', 'contenido']
    template_name = 'enviar_mensaje.html'
    success_url = reverse_lazy('mensajes_recibidos')

    def form_valid(self, form):
        form.instance.remitente = self.request.user
        return super().form_valid(form)


class MensajesRecibidos(ListView):
    model = Mensaje
    template_name = 'mensajes_recibidos.html'

    def get_queryset(self):
        return Mensaje.objects.filter(destinatario=self.request.user)
    

    
class EliminarMensaje(DeleteView):
    model = Mensaje
    template_name = 'confirmar_eliminacion.html'
    success_url = reverse_lazy('mensajes_recibidos')
   
    
    def get_queryset(self):
        queryset = super().get_queryset()
        tipo = self.kwargs.get('tipo')

        if tipo == 'recibido':
            return queryset.filter(destinatario=self.request.user)
        elif tipo == 'enviado':
            return queryset.filter(remitente=self.request.user)
        else:
            # Opcional: puedes manejar casos inesperados
            return Mensaje.objects.none()

    def get_success_url(self):
        tipo = self.kwargs.get('tipo')
        if tipo == 'recibido':
            return reverse_lazy('mensajes_recibidos')
        elif tipo == 'enviado':
            return reverse_lazy('mensajes_enviados')
        else:
            return reverse_lazy('home')  # O cualquier otra ruta por defecto