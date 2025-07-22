from django.db import models
from Aplicaciones.Animal.models import Animal
from Aplicaciones.Ubicacion.models import Ubicacion

class Grabacion(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    archivo_audio = models.FileField(upload_to='grabaciones/')
    fecha = models.DateField()
    investigador = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.animal} - {self.fecha}"
