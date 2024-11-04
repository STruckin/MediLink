from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

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

    # nombre
    # Apellidos
    # Ciudad
    # Numero de celular
    # correo electronico
    # contraseña 1
    # contraseña 2
    # cedula
    # formacion
    # experiencia
    # direccion

