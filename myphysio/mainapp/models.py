from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class LoginUserForm(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefonoP = models.IntegerField(blank=True, null=True)
    emailP = models.EmailField(blank=True, null=True)
    sintomas = models.CharField(max_length=50, blank=True, null=True)
    frecuencia_dolor = models.CharField(max_length=50, blank=True, null=True)
    act_causante = models.CharField(max_length=50, blank=True, null=True)
    descripcion_dolor = models.CharField(max_length=50, blank=True, null=True)
    intensidad_dolor = models.CharField(max_length=50, blank=True, null=True)
    tratamiento = models.CharField(max_length=50, blank=True, null=True)
    lesiones = models.CharField(max_length=50, blank=True, null=True)
    condicion = models.CharField(max_length=50, blank=True, null=True)
    tratamientos_previos = models.CharField(max_length=50, blank=True, null=True)
    medicacion_actual = models.CharField(max_length=50, blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)
    altura = models.IntegerField(blank=True, null=True)
    rango_mov = models.IntegerField(blank=True, null=True)
    presion = models.CharField(max_length=50, blank=True, null=True)
    ocupacion = models.CharField(max_length=50, blank=True, null=True)
    act_fisica = models.CharField(max_length=50, blank=True, null=True)
    descanso = models.CharField(max_length=50, blank=True, null=True)
    alimentacion = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido_paterno + ' ' + self.apellido_materno

class Receta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=False, null=False)
    diagnostico = models.CharField(max_length=255)
    fecha = models.DateField()
    alergia = models.CharField(max_length=255)
    medicamento = models.CharField(max_length=255)
    forma = models.CharField(max_length=255)
    dosis = models.CharField(max_length=255)
    via = models.CharField(max_length=255)
    duracion = models.CharField(max_length=255)
    frecuencia = models.CharField(max_length=255)
    indicaciones = models.CharField(max_length=255)

    def __str__(self):
        return self.paciente.nombre + ' ' + self.paciente.apellido_paterno + ' ' + self.paciente.apellido_materno + ' ' + self.fecha.strftime("%d/%m/%Y")


    
class Citas(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=False, null=False)
    fecha = models.DateField()
    hora =  models.TimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        print("Su cita a sido registrada correctamente")
        return self.paciente.nombre + ' ' + self.paciente.apellido_paterno + ' ' + self.paciente.apellido_materno + ' ' + self.fecha.strftime("%d/%m/%Y")
