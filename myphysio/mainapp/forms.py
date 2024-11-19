from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Paciente, ExploracionFisica, EstiloVida, Antecedentes

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
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 
                  'edad', 'nacimiento', 'direccion', 'telefonoP', 'emailP']

class ExploracionFisicaForm(forms.ModelForm):
    class Meta:
        model = ExploracionFisica
        fields = ['sexo', 'peso', 'altura', 'talla', 'imc', 'presion', 
                  'embarazo', 'trimestre']

class EstiloVidaForm(forms.ModelForm):
    class Meta:
        model = EstiloVida
        fields = ['ocupacion', 'alimentacion', 'act_fisica', 'alcohol', 
                  'cigarrillo', 'farmacos', 'especifique']

class AntecedentesForm(forms.ModelForm):
    class Meta:
        model = Antecedentes
        fields = ['diabetes', 'cancer', 'cardiopatia', 'alergias', 
                  'enfermedad_renal', 'hipertension', 'fracturas', 
                  'cirugias', 'lesiones']
