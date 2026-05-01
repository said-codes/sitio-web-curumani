from django.contrib import admin
from .models import Negocio, Evento

@admin.register(Negocio)
class NegocioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'direccion', 'telefono')
    search_fields = ('nombre', 'categoria')

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('title', 'start', 'end', 'color')
    search_fields = ('title',)
    list_filter = ('start', 'color')
