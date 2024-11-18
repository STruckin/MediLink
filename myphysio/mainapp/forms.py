from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Paciente, Receta

class RegisterUserForm(UserCreationForm):
    nombre = forms.CharField(max_length=20)
    apellido_paterno = forms.CharField(max_length=20)
    apellido_materno = forms.CharField(max_length=20)
    ciudad = forms.CharField(max_length=50)
    celular = forms.IntegerField()
    email = forms.EmailField()
    cedula = forms.IntegerField()
    formacion = forms.CharField(max_length=100)
    experiencia = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=200)
    class Meta:
        model = User
        fields = ('username', 'nombre', 'apellido_paterno', 'apellido_materno',
                   'ciudad', 'celular', 'email', 'password1', 'password2',
                    'cedula', 'formacion', 'experiencia', 'direccion')

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = "__all__"

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = "__all__"


