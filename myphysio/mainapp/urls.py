from django.urls import path
from . import views

urlpatterns = [
    path("base/", views.base, name="base"),
    path("", views.index, name="index"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("contacts/", views.contacts, name="contacts"),
    path("dashboard_home/", views.dashboard_home, name="dashboard_home"),
    path("home/", views.home, name="home"),
    path("pacientes/", views.pacientes, name="pacientes"),
    path("reg_paciente/", views.reg_paciente, name="reg_paciente"),
    path("mostrar_paciente/<paciente_id>/", views.mostrar_paciente, name="mostrar_paciente"),
    path("update_paciente/<paciente_id>", views.update_paciente, name="update_paciente"),
    path("delete_paciente/<paciente_id>", views.delete_paciente, name="delete_paciente"), 
    path("recetas/", views.recetas, name="recetas"),
    path("reg_recetas/", views.reg_recetas, name="reg_recetas"),
    path("update_receta/<receta_id>", views.update_receta, name="update_receta"),
    path("delete_receta/<receta_id>", views.delete_receta, name="delete_receta"), 
    path("citas/", views.citas, name="citas"),
    path("reg_citas/", views.reg_citas, name="reg_citas"),
    path("update_cita/<cita_id>", views.update_cita, name="update_cita"),
    path("delete_cita/<cita_id>", views.delete_cita, name="delete_cita"), 
    path("historial/", views.historial, name="historial"),
    path("reg_historial/", views.reg_historial, name="reg_historial"),
    path("historial2/", views.historial2, name="historial2"),
    
]


