from django.http import HttpResponse, Http404
from django.template import loader

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
    template = loader.get_template("./aboutus.html")
    context = {}
    return HttpResponse(template.render(context, request))

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