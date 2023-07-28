from django.urls import path
from . import views

app_name = 'tercera_preentrega_app'

urlpatterns = [
    path('', views.lista_videojuegos, name='lista_videojuegos'),
    path('videojuego/<int:pk>/', views.detalle_videojuego, name='detalle_videojuego'),
    path('consolas/', views.lista_consolas, name='lista_consolas'),
    path('consola/<int:pk>/', views.detalle_consola, name='detalle_consola'),
    path('accesorios/', views.lista_accesorios, name='lista_accesorios'),
    path('accesorio/<int:pk>/', views.detalle_accesorio, name='detalle_accesorio'),
    path('buscar/', views.buscar, name='buscar'),
]