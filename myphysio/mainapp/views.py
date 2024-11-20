from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterUserForm, PacienteForm, RecetaForm, CitaForm
from .models import Receta, Paciente, Citas
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
    info_citas = Citas.objects.all
    return render(request, "./home.html", {'all': info_citas})

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
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('El paciente fue registrado correctamente'))
            return redirect("pacientes")
    else:
        messages.success(request, ('Error'))
        form = PacienteForm()
    return render(request, "reg_paciente.html", {"form": form})

def mostrar_paciente(request, paciente_id):
    paciente = Paciente.objects.get(pk=paciente_id)
    return render(request, "mostrar_paciente.html", {"paciente": paciente})


def recetas(request):
    info_receta = Receta.objects.all
    return render(request, "./recetas.html", {'all': info_receta})

def reg_recetas (request):
    if request.method == "POST":
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('El paciente fue registrado correctamente'))
            return redirect("recetas")
    else:
        messages.success(request, ('Error'))
        form = RecetaForm()
    return render(request, "reg_recetas.html", {"form": form})

def citas(request):
    info_citas = Citas.objects.all
    return render(request, "./citas.html", {'all': info_citas})
    
def reg_citas(request):
    if request.method == "POST":
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('El paciente fue registrado correctamente'))
            return redirect("citas")
    else:
        messages.success(request, ('Error'))
        form = CitaForm()
    return render(request, "reg_citas.html", {"form": form})

def reportemedico(request):
    return render(request,"./reportemedico.html")
