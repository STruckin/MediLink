from django.db import models

# Create your models here.

class Receta(models.Model):
    paciente = models.CharField(max_length=50)
    diagnostico = models.CharField(max_length=255)
    fecha = models.DateField()
    edad = models.IntegerField()
    alergia = models.CharField(max_length=255)
    peso = models.IntegerField()
    altura = models.IntegerField()
    medicamento = models.CharField(max_length=255)
    forma = models.CharField(max_length=255)
    dosis = models.CharField(max_length=255)
    via = models.CharField(max_length=255)
    duracion = models.CharField(max_length=255)
    frecuencia = models.CharField(max_length=255)
    indicaciones = models.CharField(max_length=255)

    def __str__(self):
        return self.paciente + ' - ' + self.diagnostico