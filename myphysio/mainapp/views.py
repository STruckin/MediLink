from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterUserFormClass, PacienteForm, RecetaForm, CitaForm, HistorialFrom, LoginUserForm
from .models import Receta, Paciente, Citas, Historial, RegisterUserForm
# Create your views here.

def base(request):
    return render(request, "./base.html")

def index(request):
    return render(request, "./index.html")

def aboutus(request):
    return render(request,"./aboutus.html")

def login_view(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                user = RegisterUserForm.objects.get(username=username)
            except RegisterUserForm.DoesNotExist:
                user = None
                
            if user is not None and user.check_password(password):
                login(request, user)
                return redirect('home')
    else:
        form = LoginUserForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("./login.html")
    
def home(request):
    info_citas = Citas.objects.all
    return render(request, "./home.html", {'all': info_citas})

def register(request):
    if request.method == "POST":
        form = RegisterUserFormClass(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            return redirect("login")
            
    else:
        form = RegisterUserFormClass()
    return render(request, "./register.html", { "form": form})



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
    return render(request, "./mostrar_paciente.html", {'paciente': paciente})

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

def historial2(request):
    return render(request,"./historial2.html")

def historial(request):
    info_receta = Historial.objects.all
    return render(request, "./historial.html", {'all': info_receta})

def reg_historial (request):
    if request.method == "POST":
        form = HistorialFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('El historial fue registrado correctamente'))
            return redirect("historial")
    else:
        messages.success(request, ('Error'))
        form = HistorialFrom()
    return render(request, "reg_historial.html", {"form": form})