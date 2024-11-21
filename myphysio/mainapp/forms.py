from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django import forms
from .models import Paciente, Receta, Citas, Historial


class LoginUserForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario', 'class': 'form-input'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-input'})
    )
    
    
class RegisterUserForm(UserCreationForm):
    nombre = forms.CharField(max_length=20, 
                             widget=forms.TextInput(attrs={'class': 'short-input'}))
    apellido_paterno = forms.CharField(max_length=20,
                            widget=forms.TextInput(attrs={'placeholder': '', 'class': 'short-input'}))
    apellido_materno = forms.CharField(max_length=20,
                            widget=forms.TextInput(attrs={'placeholder': '', 'class': 'short-input'}))
    username = forms.CharField(max_length=20,
                            widget=forms.TextInput(attrs={'class': 'short-input'}))
    ciudad = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={'placeholder': '', 'class': 'form-input'}))
    celular = forms.CharField(
        max_length = 10,
        min_length=8,
        widget=forms.TextInput(attrs={'placeholder': '', 'class': 'form-input'}),
        validators=[
            RegexValidator(
                regex=r'^[2-9]{1}[0-9]{9}$',  # El número debe tener 10 dígitos y comenzar con un dígito entre 2 y 9.
                message="Introduce un número de teléfono válido de 10 dígitos sin espacios ni caracteres especiales."
            )
        ]
    )
    email = forms.EmailField(max_length=100,
                             widget=forms.TextInput(attrs={'placeholder': '', 'class': 'form-input'}))
    password1= forms.CharField(min_length=8,
                            widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2= forms.CharField(min_length=8,
                            widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    cedula = forms.IntegerField(
                                widget=forms.NumberInput(attrs={'class': 'form-input'}))
    formacion = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-input'}))
    experiencia = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'class': 'form-input'}) )
    direccion = forms.CharField(max_length=200,
                                widget=forms.TextInput(attrs={'class': 'form-input'}))
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


class CitaForm(forms.ModelForm):
    class Meta:
        model = Citas
        fields = "__all__"
        
class HistorialFrom(forms.ModelForm):
    class Meta:
        model = Historial
        fields = "__all__"