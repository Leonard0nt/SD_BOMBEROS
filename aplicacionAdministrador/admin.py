from django.contrib import admin as admin
from aplicacionAdministrador.models import * 
from aplicacionAdministrador.formsAdministrador.formsAdm import VoluntarioForm


# Register your models here.

class VoluntarioAdmin(admin.ModelAdmin):
    exclude = ('estado','unidad_asignada','cuartel_actual')
    form = VoluntarioForm  # Asegúrate de usar tu formulario personalizado aquí
    list_display = ['rut', 'nombres', 'apellidos', 'cargo', 'telefono', 'compania', 'is_staff']  # Aseguramos que 'is_staff' se vea en la lista
    list_filter = ['is_staff']  # Agregamos un filtro para 'is_staff'



class excludeElementUnidades(admin.ModelAdmin):
    exclude = ('estado_unidad','comentario','cuartel_actual')

class excludeElementAdm(admin.ModelAdmin):
    exlude = ('cuartel_seleccionado',)    



admin.site.register(voluntarios, VoluntarioAdmin)
admin.site.register(cuarteles)
admin.site.register(unidades, excludeElementUnidades)


