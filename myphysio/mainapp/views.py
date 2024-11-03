from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render

# Create your views here.

def base(request):
    template = loader.get_template("./index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template("./index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def aboutus(request):
    return render(request,"./aboutus.html")

def login(request):
    template = loader.get_template("./login.html")
    context = {}
    return HttpResponse(template.render(context, request))

def register(request):
    template = loader.get_template("register.html")
    context = {}
    return HttpResponse(template.render(context, request))

def historial(request):
    template = loader.get_template("historial.html")
    context = {}
    return HttpResponse(template.render(context, request))

def contacts(request):
    return render(request,"./contacts.html")