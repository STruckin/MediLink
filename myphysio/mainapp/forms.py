from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django import forms
from .models import Paciente, Receta, Citas, Historial, RegisterUserForm


class LoginUserForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario', 'class': 'form-input'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-input'})
    )
    
    
class RegisterUserFormClass(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'short-input'}), max_length=50)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'short-input'}), max_length=50)
    
    class Meta:
        model = RegisterUserForm
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'username', 
                  'password1', 'password2', 'email', 'ciudad', 'telefono', 
                  'cedula', 'experiencia', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'short-input'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'short-input'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'short-input'}),
            'username': forms.TextInput(attrs={'class': 'short-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-input'}),
            'telefono': forms.TextInput(attrs={'class': 'short-input', 'maxlength': '10', 'type' : 'tel'}),
            'cedula': forms.TextInput(attrs={'class': 'short-input', 'maxlength': '15'}),
            'experiencia': forms.TextInput(attrs={'class': 'form-input'}),
            'direccion': forms.TextInput(attrs={'class': 'form-input'}),
        }  
        
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        # Usamos el método set_password para encriptar la contraseña antes de guardarla
        user.set_password(self.cleaned_data['password1'])
        
        if commit:
            user.save()
        
        return user
    

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