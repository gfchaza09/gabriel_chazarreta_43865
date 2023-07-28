from django.contrib import admin
from .models import Videojuego, Consola, Accesorio

class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'desarrollador', 'año_lanzamiento')
    search_fields = ('titulo', 'genero', 'desarrollador')

class ConsolaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fabricante', 'año_lanzamiento')
    search_fields = ('nombre', 'fabricante')

class AccesorioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo')
    search_fields = ('nombre', 'tipo')

admin.site.register(Videojuego, VideojuegoAdmin)
admin.site.register(Consola, ConsolaAdmin)
admin.site.register(Accesorio, AccesorioAdmin)
