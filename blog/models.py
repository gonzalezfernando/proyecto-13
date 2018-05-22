from django.db import models
from django.utils import timezone
# Create your models here.
class Receta(models.Model):
    Titulo = models.CharField(max_length=200)
    Ingredientes = models.TextField()
    Preparacion = models.TextField()
    Fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def publicacion(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
