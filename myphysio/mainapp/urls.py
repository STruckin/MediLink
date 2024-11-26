from django.urls import path
from . import views

urlpatterns = [
    # Pagina de inicio    
    path("base/", views.base, name="base"),
    path("", views.index, name="index"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("contacts/", views.contacts, name="contacts"),
    
    ## Dashboard para pacientes
    path("dashboard_homepa/", views.dashboard_homepa, name="dashboard_homepa"),
    path("home/", views.home, name="home"),
    path("loginpa/", views.loginpa, name="loginpa"),
    path("citaspa/", views.citaspa, name="citaspa"),
    path("historialpa/", views.historialpa, name="historialpa"),
    path("recetaspa/", views.recetaspa, name="recetaspa"),
    
    #Citas paciente
    path("reg_citaspa/", views.reg_citaspa, name="reg_citaspa"),
    
    #Historial paciente
    path("reg_historialpa/", views.reg_historialpa, name="reg_historialpa"),
    
    #Recetas paciente
    path("reg_recetaspa/", views.reg_recetaspa, name="reg_recetaspa"),
    
    
    # Dashboard para usuarios (medicos)
    path("dashboard_home/", views.dashboard_home, name="dashboard_home"),
    path("home/", views.home, name="home"),

    # Pacientes
    path("pacientes/", views.pacientes, name="pacientes"),
    path("reg_paciente/", views.reg_paciente, name="reg_paciente"),
    path("mostrar_paciente/<paciente_id>/", views.mostrar_paciente, name="mostrar_paciente"),
    path("update_paciente/<paciente_id>", views.update_paciente, name="update_paciente"),
    path("delete_paciente/<paciente_id>", views.delete_paciente, name="delete_paciente"), 

    # Recetas
    path("recetas/", views.recetas, name="recetas"),
    path("reg_recetas/", views.reg_recetas, name="reg_recetas"),
    path("update_receta/<receta_id>", views.update_receta, name="update_receta"),
    path("delete_receta/<receta_id>", views.delete_receta, name="delete_receta"),
    path("pdf_receta/<receta_id>", views.pdf_receta, name="pdf_receta"),  

    # Citas
    path("citas/", views.citas, name="citas"),
    path("reg_citas/", views.reg_citas, name="reg_citas"),
    path("update_cita/<cita_id>", views.update_cita, name="update_cita"),
    path("delete_cita/<cita_id>", views.delete_cita, name="delete_cita"), 

    # Historiales
    path("historial/", views.historial, name="historial"),
    path("reg_historial/", views.reg_historial, name="reg_historial"),
    path("historial2/", views.historial2, name="historial2"),
    path("mostrar_historial/<historial_id>/", views.mostrar_historial, name="mostrar_historial"),
    path("update_historial/<historial_id>", views.update_historial, name="update_historial"),
    path("delete_historial/<historial_id>", views.delete_historial, name="delete_historial"),
    path("pdf_historial/<historial_id>", views.pdf_historial, name="pdf_historial"),      

    # Reportes
    path("reportemedico/", views.reportemedico, name="reportemedico"),     
    path("reg_reporte/", views.reg_reporte, name="reg_reporte"),
    path("update_reporte/<reporte_id>", views.update_reporte, name="update_reporte"),
    path("delete_reporte/<reporte_id>", views.delete_reporte, name="delete_reporte"),  
    path("pdf_reporte/<reporte_id>", views.pdf_reporte, name="pdf_reporte"),     

]
