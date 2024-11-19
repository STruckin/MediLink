from django.db import models
from django.utils import timezone 

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    edad = models.IntegerField()
    nacimiento = models.DateField(default=timezone.now)
    direccion = models.CharField(max_length=50)
    telefonoP = models.IntegerField()
    emailP = models.EmailField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido_paterno + ' ' + self.apellido_materno
    

class ExploracionFisica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    sexo = models.CharField(max_length=50)
    peso = models.IntegerField()
    altura = models.IntegerField()
    talla = models.IntegerField()
    imc = models.IntegerField()
    presion = models.CharField(max_length=50)
    embarazo = models.BooleanField(default=False)
    trimestre = models.CharField(max_length=50, blank=True, null=True)  # Trimestre puede estar vacío

    def __str__(self):
        return f"{self.paciente} - Exploración Física"
    

class EstiloVida(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    ocupacion = models.CharField(max_length=50)
    alimentacion = models.CharField(max_length=50)
    act_fisica = models.CharField(max_length=50)
    alcohol = models.BooleanField(default=False)
    cigarrillo = models.BooleanField(default=False)
    farmacos = models.BooleanField(default=False)  # Cambiado para evitar caracteres especiales
    especifique = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.paciente} - Estilo de Vida"


class Antecedentes(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    diabetes = models.BooleanField(default=False)  # Ajustado para mayor claridad
    cancer = models.BooleanField(default=False)
    cardiopatia = models.BooleanField(default=False)  # Corregido nombre
    alergias = models.CharField(max_length=50, blank=True, null=True)
    enfermedad_renal = models.BooleanField(default=False)  # Ajustado y renombrado
    hipertension = models.BooleanField(default=False)  # Corregido para ser más claro
    fracturas = models.CharField(max_length=50, blank=True, null=True)
    cirugias = models.CharField(max_length=50, blank=True, null=True)
    lesiones = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.paciente} - Antecedentes"


class Receta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    diagnostico = models.CharField(max_length=255)
    fecha = models.DateField()
    edad = models.IntegerField()
    alergia = models.CharField(max_length=255, blank=True, null=True)
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
        return f"{self.paciente} - {self.diagnostico}"
  