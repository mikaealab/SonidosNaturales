from django.db import models

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=100)
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
