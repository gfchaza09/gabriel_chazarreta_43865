from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'tercera_preentrega_app'

urlpatterns = [
    path('', views.login_request, name='login'),
    path('acerca_de/', views.acerca_de, name='acerca_de'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('videojuegos/', views.lista_videojuegos, name='lista_videojuegos'),
    path('videojuego/<int:pk>/', views.detalle_videojuego, name='detalle_videojuego'),
    path('videojuego/<int:pk>/editar/', views.editar_videojuego, name='editar_videojuego'),
    path('videojuego/<int:pk>/eliminar/', views.eliminar_videojuego, name='eliminar_videojuego'),
    path('consolas/', views.lista_consolas, name='lista_consolas'),
    path('consola/<int:pk>/', views.detalle_consola, name='detalle_consola'),
    path('consola/<int:pk>/editar', views.editar_consola, name='editar_consola'),
    path('consola/<int:pk>/eliminar', views.eliminar_consola, name='eliminar_consola'),
    path('accesorios/', views.lista_accesorios, name='lista_accesorios'),
    path('accesorio/<int:pk>/', views.detalle_accesorio, name='detalle_accesorio'),
    path('accesorio/<int:pk>/editar', views.editar_accesorio, name='editar_accesorio'),
    path('accesorio/<int:pk>/eliminar', views.eliminar_accesorio, name='eliminar_accesorio'),
    path('buscar/', views.buscar, name='buscar'),
    path('registro/', views.register, name='registro'),
    path('logout', LogoutView.as_view(template_name='tercera_preentrega_app/logout.html'), name='logout'),
]