from django.db import models


class Videojuego(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    desarrollador = models.CharField(max_length=100)
    año_lanzamiento = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo

class Consola(models.Model):
    nombre = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    año_lanzamiento = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

class Accesorio(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
