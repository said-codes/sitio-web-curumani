from django.db import models

class Negocio(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=50)
    horario = models.CharField(max_length=200)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    title = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    color = models.CharField(max_length=50, default="#005A8D")

    def __str__(self):
        return self.title
