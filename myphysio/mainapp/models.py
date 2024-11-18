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
    
class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefonoP = models.IntegerField()
    emailP = models.EmailField()
    sintomas = models.CharField(max_length=50)
    frecuencia_dolor = models.CharField(max_length=50)
    act_causante = models.CharField(max_length=50)
    descripcion_dolor = models.CharField(max_length=50)
    intensidad_dolor = models.CharField(max_length=50)
    tratamiento = models.CharField(max_length=50)
    lesiones = models.CharField(max_length=50)
    condicion = models.CharField(max_length=50)
    tratamientos_previos = models.CharField(max_length=50)
    medicacion_actual = models.CharField(max_length=50)
    peso = models.IntegerField()
    altura = models.IntegerField()
    rango_mov = models.IntegerField()
    presion = models.CharField(max_length=50)
    ocupacion = models.CharField(max_length=50)
    act_fisica = models.CharField(max_length=50)
    descanso = models.CharField(max_length=50)
    alimentacion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + ' ' + self.apellido_paterno + ' ' + self.apellido_materno