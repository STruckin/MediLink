from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from datetime import datetime, date
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


# Create your models here.

class LoginUserForm(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
class RegisterUserForm(models.Model):
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    ciudad = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10,blank=True, null=True)
    cedula = models.CharField(max_length=15, blank=True, null=True)
    experiencia = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    
    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username + self.nombre

    def set_password(self, password):
        """Método para encriptar la contraseña antes de guardarla."""
        self.password = make_password(password)

    def check_password(self, password):
        """Método para verificar la contraseña."""
        from django.contrib.auth.hashers import check_password
        return check_password(password, self.password)
    

    
class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    edad = models.IntegerField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    telefonoP = models.CharField(max_length=10,blank=True, null=True)
    emailP = models.EmailField(blank=True, null=True)
    sintomas = models.CharField(max_length=100, blank=True, null=True)
    frecuencia_dolor = models.CharField(max_length=255, blank=True, null=True)
    act_causante = models.CharField(max_length=100, blank=True, null=True)
    descripcion_dolor = models.CharField(max_length=100, blank=True, null=True)
    intensidad_dolor = models.CharField(max_length=100, blank=True, null=True)
    tratamiento = models.TextField(max_length=255, blank=True, null=True)
    lesiones = models.CharField(max_length=100, blank=True, null=True)
    condicion = models.CharField(max_length=100, blank=True, null=True)
    tratamientos_previos = models.TextField(max_length=255, blank=True, null=True)
    medicacion_actual = models.CharField(max_length=100, blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)
    altura = models.IntegerField(blank=True, null=True)
    rango_mov = models.IntegerField(blank=True, null=True)
    presion = models.CharField(max_length=100, blank=True, null=True)
    ocupacion = models.CharField(max_length=100, blank=True, null=True)
    act_fisica = models.CharField(max_length=100, blank=True, null=True)
    descanso = models.TextField(max_length=255, blank=True, null=True)
    alimentacion = models.TextField(max_length=255, blank=True, null=True)

    
    def save(self, *args, **kwargs):
        if self.fecha_nacimiento:
            today = date.today()
            self.edad = today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("paciente-detail", kwargs={"pk": self.pk})

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


    
from django.core.exceptions import ValidationError

class Citas(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=False, null=False)
    fecha = models.DateField()
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    
    class Meta:
        unique_together = ('paciente', 'fecha', 'hora')

    def __str__(self):
        return f"{self.paciente.nombre} {self.fecha.strftime('%d/%m/%Y')} {self.hora.strftime('%H:%M')}"

    def clean(self):
        # Validar si ya existe una cita en la misma fecha y hora para el paciente
        if Citas.objects.filter(
            paciente=self.paciente,
            fecha=self.fecha,
            hora=self.hora
        ).exclude(pk=self.pk).exists():
            raise ValidationError(f"El paciente {self.paciente} ya tiene una cita en esta fecha y hora.")


class Historial(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=False, null=False)
    fecha = models.DateField()
    #Evaluación Muscular
    cuello_d = models.IntegerField(blank=True, null=True)
    torso_d = models.IntegerField(blank=True, null=True)
    m_sup_d = models.IntegerField(blank=True, null=True)
    m_inf_d = models.IntegerField(blank=True, null=True)
    cuello_i = models.IntegerField(blank=True, null=True)
    torso_i = models.IntegerField(blank=True, null=True)
    m_sup_i = models.IntegerField(blank=True, null=True)
    m_inf_i = models.IntegerField(blank=True, null=True)
    #Evaluación Goniométrica
    cuello_dg = models.IntegerField(blank=True, null=True)
    torso_dg = models.IntegerField(blank=True, null=True)
    m_sup_dg = models.IntegerField(blank=True, null=True)
    m_inf_dg = models.IntegerField(blank=True, null=True)
    cuello_ig = models.IntegerField(blank=True, null=True)
    torso_ig = models.IntegerField(blank=True, null=True)
    m_sup_ig = models.IntegerField(blank=True, null=True)
    m_inf_ig = models.IntegerField(blank=True, null=True)
    # Evaluación Miembros Superiores / Hombro
    flexv_ms_hd = models.IntegerField(blank=True, null=True)
    flexh_ms_hd = models.IntegerField(blank=True, null=True)
    extv_ms_hd = models.IntegerField(blank=True, null=True)
    exth_ms_hd = models.IntegerField(blank=True, null=True)
    abd_ms_hd = models.IntegerField(blank=True, null=True)
    add_ms_hd = models.IntegerField(blank=True, null=True)
    rotext_ms_hd = models.IntegerField(blank=True, null=True)
    rotint_ms_hd = models.IntegerField(blank=True, null=True)
    flexv_ms_hi = models.IntegerField(blank=True, null=True)
    flexh_ms_hi = models.IntegerField(blank=True, null=True)
    extv_ms_hi = models.IntegerField(blank=True, null=True)
    exth_ms_hi = models.IntegerField(blank=True, null=True)
    abd_ms_hi = models.IntegerField(blank=True, null=True)
    add_ms_hi = models.IntegerField(blank=True, null=True)
    rotext_ms_hi = models.IntegerField(blank=True, null=True)
    rotint_ms_hi = models.IntegerField(blank=True, null=True)
    # Evaluación Miembros Superiores / Brazo
    flex_ms_bd = models.IntegerField(blank=True, null=True)
    ext_ms_bd = models.IntegerField(blank=True, null=True)
    pron_ms_bd = models.IntegerField(blank=True, null=True)
    susp_ms_bd = models.IntegerField(blank=True, null=True)
    flex_ms_bi = models.IntegerField(blank=True, null=True)
    ext_ms_bi = models.IntegerField(blank=True, null=True)
    pron_ms_bi = models.IntegerField(blank=True, null=True)
    susp_ms_bi = models.IntegerField(blank=True, null=True)
    # Evaluación Miembros Superiores / Muñeca
    flex_ms_md = models.IntegerField(blank=True, null=True)
    ext_ms_md = models.IntegerField(blank=True, null=True)
    abdr_ms_md = models.IntegerField(blank=True, null=True)
    add_ms_md = models.IntegerField(blank=True, null=True)
    flex_ms_mi = models.IntegerField(blank=True, null=True)
    ext_ms_mi = models.IntegerField(blank=True, null=True)
    abdr_ms_mi = models.IntegerField(blank=True, null=True)
    add_ms_mi = models.IntegerField(blank=True, null=True)
    #Evaluación Miembros Inferior / Cadera
    flex_mi_cd = models.IntegerField(blank=True, null=True)
    ext_mi_cd = models.IntegerField(blank=True, null=True)
    flexcr_mi_cd = models.IntegerField(blank=True, null=True)
    abd_mi_cd = models.IntegerField(blank=True, null=True)
    add_mi_cd = models.IntegerField(blank=True, null=True)
    rotint_mi_cd = models.IntegerField(blank=True, null=True)
    rotext_mi_cd = models.IntegerField(blank=True, null=True)
    flex_mi_ci = models.IntegerField(blank=True, null=True)
    ext_mi_ci = models.IntegerField(blank=True, null=True)
    flexcr_mi_ci = models.IntegerField(blank=True, null=True)
    abd_mi_ci = models.IntegerField(blank=True, null=True)
    add_mi_ci = models.IntegerField(blank=True, null=True)
    rotint_mi_ci = models.IntegerField(blank=True, null=True)
    rotext_mi_ci = models.IntegerField(blank=True, null=True)
    #Evaluación Miembros Inferior / Piernas
    flex_mi_pd = models.IntegerField(blank=True, null=True)
    ext_mi_pd = models.IntegerField(blank=True, null=True)
    rotint_mi_pd = models.IntegerField(blank=True, null=True)
    rotext_mi_pd = models.IntegerField(blank=True, null=True)
    flexplan_mi_pd = models.IntegerField(blank=True, null=True)
    dors_mi_pd = models.IntegerField(blank=True, null=True)
    inve_mi_pd = models.IntegerField(blank=True, null=True)
    ever_mi_pd = models.IntegerField(blank=True, null=True)
    flex_mi_pi = models.IntegerField(blank=True, null=True)
    ext_mi_pi = models.IntegerField(blank=True, null=True)
    rotint_mi_pi = models.IntegerField(blank=True, null=True)
    rotext_mi_pi = models.IntegerField(blank=True, null=True)
    flexplan_mi_pi = models.IntegerField(blank=True, null=True)
    dors_mi_pi = models.IntegerField(blank=True, null=True)
    inve_mi_pi = models.IntegerField(blank=True, null=True)
    ever_mi_pi = models.IntegerField(blank=True, null=True)
    #Evaluación Marcha / Deambulación
    pres_dif = models.CharField(max_length=250, blank=True, null=True)
    pres_ayud = models.CharField(max_length=250, blank=True, null=True)
    pres_claudi = models.CharField(max_length=250, blank=True, null=True)
    pres_atax = models.CharField(max_length=250, blank=True, null=True)
    pres_espa = models.CharField(max_length=250, blank=True, null=True)
    
    
    def __str__(self):
        return self.paciente.nombre + ' ' + self.paciente.apellido_paterno + ' ' + self.paciente.apellido_materno + ' ' + self.fecha.strftime("%d/%m/%Y")

class Reporte(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=False, null=False)
    diagnostico = models.CharField(max_length=255)
    fecha = models.DateField()
    motivoconsulta = models.TextField(max_length=555)
    descripcion = models.TextField(max_length=555)
    compromisos = models.TextField(max_length=555)
    fechasnconsulta = models.DateField()
    horanconsulta = models.TimeField(null=True, blank=True)  # Nuevo campo para la hora

    def __str__(self):
        return f"{self.paciente.nombre} {self.fecha.strftime('%d/%m/%Y')}"