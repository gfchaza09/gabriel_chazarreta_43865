from django.contrib.auth.models import User
from django.db import models

def user_directory_path(instance, filename):
    # El archivo se subirá a MEDIA_ROOT/user_<id>/<filename>
    return f'user_{instance.user.id}/{filename}'

class Videojuego(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    desarrollador = models.CharField(max_length=100)
    año_lanzamiento = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo
    
    def get_tipo(self):
        return 'Videojuego'

class Consola(models.Model):
    nombre = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    año_lanzamiento = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
    
    def get_tipo(self):
        return 'Consola'

class Accesorio(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    def get_tipo(self):
        return 'Accesorio'
    

class Review(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE, null=True, blank=True)
    consola = models.ForeignKey(Consola, on_delete=models.CASCADE, null=True, blank=True)
    accesorio = models.ForeignKey(Accesorio, on_delete=models.CASCADE, null=True, blank=True)
    calificacion = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.videojuego:
            return f'Reseña de {self.videojuego.titulo} por {self.usuario.username}'
        elif self.consola:
            return f'Reseña de {self.consola.nombre} por {self.usuario.username}'
        elif self.accesorio:
            return f'Reseña de {self.accesorio.nombre} por {self.usuario.username}'

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=user_directory_path, blank=True)

    def __str__(self):
        return self.user.username