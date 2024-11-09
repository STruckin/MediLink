from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("base/", views.base, name="base"),
    path("historial/", views.historial, name="historial"),
    path("contacts/", views.contacts, name="contacts"),
    path("dashboard_home/", views.dashboard_home, name="dashboard_home"),
]


