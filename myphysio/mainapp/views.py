from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PacienteForm, ExploracionFisicaForm, EstiloVidaForm, AntecedentesForm
from .models import Receta, Paciente
# Create your views here.

def base(request):
    return render(request, "./base.html")

def index(request):
    return render(request, "./index.html")

def aboutus(request):
    return render(request,"./aboutus.html")

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboard_home")
    else:
        form = AuthenticationForm()
    return render(request, "./login.html", { "form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("./index.html")
    
def home(request):
    return render(request, "./home.html")

def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("login")
            messages.success(request, ("Registro completado"))
    else:
        form = RegisterUserForm()
    return render(request, "./register.html", { "form": form})

def historial(request):
    return render(request, "./historial.html")

def contacts(request):
    return render(request,"./contacts.html")

def dashboard_home(request):
    return render(request,"./dashboard_home.html")

def pacientes(request):
    info_paciente = Paciente.objects.all
    return render(request, "./pacientes.html", {'all': info_paciente})

def reg_paciente(request):
    if request.method == "POST":
        paciente_form = PacienteForm(request.POST)
        exploracion_form = ExploracionFisicaForm(request.POST)
        estilo_vida_form = EstiloVidaForm(request.POST)
        antecedentes_form = AntecedentesForm(request.POST)

        if paciente_form.is_valid() and exploracion_form.is_valid() and estilo_vida_form.is_valid() and antecedentes_form.is_valid():
            try:
                with transaction.atomic():
                    paciente = paciente_form.save()

                    exploracion_fisica = exploracion_form.save(commit=False)
                    exploracion_fisica.paciente = paciente
                    exploracion_fisica.save()

                    estilo_vida = estilo_vida_form.save(commit=False)
                    estilo_vida.paciente = paciente
                    estilo_vida.save()

                    antecedentes = antecedentes_form.save(commit=False)
                    antecedentes.paciente = paciente
                    antecedentes.save()

                messages.success(request, "Paciente registrado exitosamente.")
                return redirect("pacientes")
            except Exception as e:
                messages.error(request, f"Error al registrar el paciente: {str(e)}")
        else:
            messages.error(request, "Formulario inválido. Por favor revisa los datos ingresados.")
    else:
        paciente_form = PacienteForm()
        exploracion_form = ExploracionFisicaForm()
        estilo_vida_form = EstiloVidaForm()
        antecedentes_form = AntecedentesForm()

    return render(request, "./reg_paciente.html", {
        "paciente_form": paciente_form,
        "exploracion_form": exploracion_form,
        "estilo_vida_form": estilo_vida_form,
        "antecedentes_form": antecedentes_form
    })
    
def recetas(request):
    info_receta = Receta.objects.all
    return render(request, "./recetas.html", {'all': info_receta})

def reg_recetas (request):
    return render(request, "./reg_recetas.html")