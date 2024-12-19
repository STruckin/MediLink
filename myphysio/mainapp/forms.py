from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django import forms
from .models import Paciente, Receta, Citas, Historial, RegisterUserForm, Reporte


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
            'telefono': forms.TextInput(attrs={'class': 'short-input', 'maxlength': '10', 'type' : 'tel', 'pattern': r'\d*', 'oninput': 'this.value=this.value.replace(/[^0-9]/g, "")'}),
            'cedula': forms.TextInput(attrs={'class': 'short-input', 'maxlength': '15', 'oninput': 'this.value=this.value.replace(/[^0-9]/g, "")'}),
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
    CATEGORY_CHOICES_SEX = [
            ('Femenino', 'Femenino'),
            ('Masculino', 'Masculino'),
            ('Otro', 'Sin especificar'),
        ]
    CATEGORY_CHOICES_FREQUENCY = [
            ('Alta', 'Alta'),
            ('Mediana', 'Mediana'),
            ('Baja', 'Baja'),
        ]
    CATEGORY_CHOICES_PAIN = [
            ('Fuerte', 'Fuerte'),
            ('Media', 'Media'),
            ('Baja', 'Baja'),
        ]
    sexo = forms.ChoiceField(choices=CATEGORY_CHOICES_SEX, widget=forms.Select())
    frecuencia_dolor = forms.ChoiceField(choices=CATEGORY_CHOICES_FREQUENCY, widget=forms.Select())
    intensidad_dolor = forms.ChoiceField(choices=CATEGORY_CHOICES_PAIN, widget=forms.Select())
    class Meta:
        model = Paciente
        fields = "__all__"
        widgets = {
            'telefonoP': forms.TextInput(attrs={'class': 'short-input', 'maxlength': '10', 'type' : 'tel', 'pattern': r'\d*', 'oninput': 'this.value=this.value.replace(/[^0-9]/g, "")'}),
            'peso' : forms.NumberInput(attrs={'class': 'short-input', 'oninput': 'this.value=this.value.slice(0,3); if (this.value < 0) this.value = 0; else if (this.value > 250) this.value = 250;'}),
            'altura' : forms.NumberInput(attrs={'class': 'short-input', 'oninput': 'this.value=this.value.slice(0,3); if (this.value < 0) this.value = 0; else if (this.value > 230) this.value = 230;'}),
            'rango_mov' : forms.NumberInput(attrs={'class': 'short-input', 'oninput': 'this.value=this.value.slice(0,2); if (this.value < 0) this.value = 0; else if (this.value > 10) this.value = 10;'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'short-input'}),
        }
        
         

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
        widgets = {
            'cuello_d': forms.NumberInput(attrs={'min': 0, 'max': 5}),
            'torso_d': forms.NumberInput(attrs={'min': 0, 'max': 5}),
            'm_sup_d': forms.NumberInput(attrs={'min': 0, 'max': 5}),
            'm_inf_d': forms.NumberInput(attrs={'min': 0, 'max': 5}),
            'cuello_i': forms.NumberInput(attrs={'min': 0, 'max': 5}),
            'torso_i': forms.NumberInput(attrs={'min': 0, 'max': 5}),
            'm_sup_i': forms.NumberInput(attrs={'min': 0, 'max': 5}),
            'm_inf_i': forms.NumberInput(attrs={'min': 0, 'max': 5}),
        }
        
        
class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = "__all__"
        widgets = {
            'horanconsulta': forms.TimeInput(attrs={'type': 'time'}),
        }

        