from django.contrib import admin
from .models import Receta, Paciente, ExploracionFisica, EstiloVida, Antecedentes

# Register your models here.
admin.site.register(Receta)
admin.site.register(Paciente)
admin.site.register(ExploracionFisica)
admin.site.register(EstiloVida)
admin.site.register(Antecedentes)