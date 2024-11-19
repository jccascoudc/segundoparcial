from django.contrib import admin
from .models import Mensaje

# Register your models here.

class MensajeAdmin(admin.ModelAdmin):
    list_display = ("remitente", "destinatario", "contenido" )
    list_filter = ("destinatario",)
    actions = ['vaciar_contenido']

    def vaciar_contenido(self,request,queryset):
        queryset.update(contenido='VACÍO')
    vaciar_contenido.short_description = 'Vacía los contenidos seleccionados'

admin.site.register(Mensaje, MensajeAdmin)