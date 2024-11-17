from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterUserForm
from .models import Receta
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

def reg_paciente(request):
    return render(request, "./reg_paciente.html")

def recetas(request):
    info_receta = Receta.objects.all
    return render(request, "./recetas.html", {'all': info_receta})