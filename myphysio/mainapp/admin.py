from django.contrib import admin
from .models import Receta, Paciente, Citas, Historial,RegisterUserForm, Reporte

# Register your models here.
admin.site.register(RegisterUserForm)
admin.site.register(Receta)
admin.site.register(Paciente)
admin.site.register(Citas)
admin.site.register(Historial)
admin.site.register(Reporte)