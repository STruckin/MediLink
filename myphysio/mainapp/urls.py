from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("base/", views.base, name="base"),
    path("historial2/", views.historial2, name="historial2"),
    path("contacts/", views.contacts, name="contacts"),
    path("dashboard_home/", views.dashboard_home, name="dashboard_home"),
    path("home/", views.home, name="home"),
    path("reg_paciente/", views.reg_paciente, name="reg_paciente"),
    path("pacientes/", views.pacientes, name="pacientes"),
    path("reg_recetas/", views.reg_recetas, name="reg_recetas"),
    path("recetas/", views.recetas, name="recetas"),
    path("citas/", views.citas, name="citas"),
    path("reg_citas/", views.reg_citas, name="reg_citas"),
     path("historial/", views.historial, name="historial"),
    path("reg_historial/", views.reg_historial, name="reg_historial"),
    
]


