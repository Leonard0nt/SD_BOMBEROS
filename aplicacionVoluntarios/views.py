import base64
from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from aplicacionAdministrador.models import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from aplicacionVoluntarios.formsVoluntario.formsVol import VoluntarioEditForm
from aplicacionVoluntarios.formsVoluntario.formsVolPass import ContrasenaEditForm



# Create your views here.
img = "../static/Bomberos.png" 


# renderiza principal ventana de voluntarios
@login_required    
def homeVoluntarios(request):
    cuartelesBuscado= cuarteles.objects.all()
    VoluntarioBuscado = request.user
    # Comprobar si el voluntario tiene cuartel_actual como null y asignar un valor (en este caso, cuartel con id=1)
    if VoluntarioBuscado.cuartel_actual_vol is None:
        # Asignamos el cuartel con id=1, asegúrate de que exista en la base de datos
        cuartel_default = cuarteles.objects.filter(idCuartel=1).first()  # O el ID que prefieras
        if cuartel_default:
            VoluntarioBuscado.cuartel_actual_vol = cuartel_default
            VoluntarioBuscado.save()  # Guardamos el cambio en la base de datos
    contexto = {'img': img,'voluntario':VoluntarioBuscado,'cuarteles': cuartelesBuscado,}
    return render(request,  "../templates/templatesVoluntario/indexVoluntario.html",contexto)

# permite obtener todos los cuarteles para poder verlos y seleccionar uno
def obtener_opciones_cuartel(request):
    cuarteles = cuarteles.objects.all()  # Obtengo todos los cuarteles en una variable
    data = [{'id': cuartel.idCuartel, 'nombre': cuartel.nombre_cuartel} for cuartel in cuarteles] #Extraigo el id y el nombre de cada cuartel 
    return JsonResponse(data, safe=False)


# actualiza el estado del voluntario segun en que boton este clickeado 
def actualizar_estado_voluntario(request):
    #cambio de estado
    if request.method == 'POST':
        nvoestado = request.POST.get('options-outlined')  # obtengo el valor del boton clickeado

        voluntario = request.user

        if nvoestado == 'disp':
            voluntario.estado = True  # Si el boton devuelve que se marco disp se activa la disponibilidad
        else:
            voluntario.estado = False  # caso contrario por defecto se desactiva la disponibilidad

        voluntario.save()  # Guarda el cambio en la base de datos

        return redirect(homeVoluntarios)
    

# luego de seleccionar actualiza el cuartel seleccionado
def actualizar_cuartel_voluntario(request):
    #cambio de cuartel
    if request.method == 'POST':
        nvoCuartel = request.POST.get('cuartelActual') # Obtengo el id del nuevo cuartel extraido del boton clickeado 
        cuartelNvo = cuarteles.objects.get(idCuartel = nvoCuartel) # busco y asigno el nuevo cuartel a una variable
        voluntario = request.user # busco el voluntario actual usando la app

        voluntario.cuartel_actual_vol = cuartelNvo # cambio la fk del cuartel por la extraida anteriormente

        voluntario.save() # guardo los cambios

        return redirect(homeVoluntarios)
 
# luego de seleccionar actualiza la disponibilidad seleccionada
def actualizar_disp_cuart(request): # funcion que realiza el cambio de disponibilidad y cuartel a la vez
    actualizar_estado_voluntario(request)
    actualizar_cuartel_voluntario(request)

    return redirect(homeVoluntarios)


# devuelve principales datos del cuartel actual seleccionado
def verCuartelActual(request,idCuartel):
    idCuartell = idCuartel
    VoluntarioBuscado = request.user
    cuartelesBuscado= cuarteles.objects.get(idCuartel=idCuartell)
    cuartelesBuscado.voluntarios_in = voluntarios.objects.filter(cuartel_actual_vol = idCuartell, estado = True ).count()
    cuartelesBuscado.unidades_in = unidades.objects.filter(cuartel_actual_uni = idCuartell, estado_unidad = True ).count()
    contexto = {
        'voluntario': VoluntarioBuscado,
        'cuartel': cuartelesBuscado,
        'img' : img,
        }
    return render(request, "../templates/templatesVoluntario/cuartelActualInfo.html", contexto)


# permite editar datos los cuales pueden ser editados por el propio usuario
def edit_voluntario(request, rut):
    voluntario = get_object_or_404(voluntarios, rut=rut)
    
    if request.method == 'POST':
        form = VoluntarioEditForm(request.POST, instance=voluntario)
        if form.is_valid():
            form.save()
            return redirect(reverse('voluntario'))
    else:
        form = VoluntarioEditForm(instance=voluntario)

    return render(request, '../templates/templatesVoluntario/configPerfil.html', {'form': form, 'voluntario': voluntario})

# permite editar contrasena 
def edit_contrasena(request, rut):
    voluntario = get_object_or_404(voluntarios, rut=rut)
    
    if request.method == 'POST':
        form = ContrasenaEditForm(request.POST, instance=voluntario)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = ContrasenaEditForm(instance=voluntario)

    return render(request, '../templates/templatesVoluntario/cambiarContra.html', {'form': form, 'voluntario': voluntario})