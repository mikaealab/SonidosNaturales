from django.db import models

class Animal(models.Model):
    nombre_comun = models.CharField(max_length=100)
    nombre_cientifico = models.CharField(max_length=150, blank=True)
    tipo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='animales/', blank=True, null=True)

    def __str__(self):
        return self.nombre_comun
