from django.contrib import admin
from .models import Videojuego, Consola, Accesorio, Perfil, Review

class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'desarrollador', 'año_lanzamiento')
    search_fields = ('titulo', 'genero', 'desarrollador')

class ConsolaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fabricante', 'año_lanzamiento')
    search_fields = ('nombre', 'fabricante')

class AccesorioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo')
    search_fields = ('nombre', 'tipo')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'videojuego', 'calificacion', 'fecha')
    search_fields = ('usuario__username', 'videojuego__titulo')
    list_filter = ('calificacion', 'fecha')

admin.site.register(Videojuego, VideojuegoAdmin)
admin.site.register(Consola, ConsolaAdmin)
admin.site.register(Accesorio, AccesorioAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Perfil)