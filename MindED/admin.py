from django.contrib import admin
from .models import paciente,intervencion

# Register your models here.

admin.site.register(paciente)

@admin.register(intervencion)
class IntervencionAdmin(admin.ModelAdmin):
    list_display = ('paciente_id', 'titulo', 'resultado_prediccion') 