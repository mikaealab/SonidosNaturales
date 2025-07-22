from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Grabacion
from animal.models import Animal
from ubicacion.models import Ubicacion

# Listar grabaciones
def listaGrabaciones(request):
    grabaciones = Grabacion.objects.all()
    return render(request, 'grabacion/lista.html', {'grabaciones': grabaciones})

# Formulario nuevo
def nuevaGrabacion(request):
    animales = Animal.objects.all()
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'grabacion/nuevo.html', {
        'animales': animales,
        'ubicaciones': ubicaciones
    })

# Guardar grabación
def guardarGrabacion(request):
    animal_id = request.POST["animal"]
    ubicacion_id = request.POST["ubicacion"]
    archivo_audio = request.FILES.get("archivo_audio")
    fecha = request.POST["fecha"]
    investigador = request.POST["investigador"]
    observaciones = request.POST["observaciones"]

    Grabacion.objects.create(
        animal_id=animal_id,
        ubicacion_id=ubicacion_id,
        archivo_audio=archivo_audio,
        fecha=fecha,
        investigador=investigador,
        observaciones=observaciones
    )

    messages.success(request, "Grabación CREADA exitosamente")
    return redirect('/grabacion/')

# Eliminar grabación
def eliminarGrabacion(request, id):
    grabacion = Grabacion.objects.get(id=id)
    grabacion.delete()
    messages.success(request, "Grabación ELIMINADA exitosamente")
    return redirect('/grabacion/')

# Formulario editar
def editarGrabacion(request, id):
    grabacionEditar = Grabacion.objects.get(id=id)
    animales = Animal.objects.all()
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'grabacion/editar.html', {
        'grabacionEditar': grabacionEditar,
        'animales': animales,
        'ubicaciones': ubicaciones
    })

# Procesar edición
def procesarEdicionGrabacion(request):
    id = request.POST["id"]
    animal_id = request.POST["animal"]
    ubicacion_id = request.POST["ubicacion"]
    archivo_audio = request.FILES.get("archivo_audio", None)
    fecha = request.POST["fecha"]
    investigador = request.POST["investigador"]
    observaciones = request.POST["observaciones"]

    grabacion = Grabacion.objects.get(id=id)
    grabacion.animal_id = animal_id
    grabacion.ubicacion_id = ubicacion_id
    grabacion.fecha = fecha
    grabacion.investigador = investigador
    grabacion.observaciones = observaciones
    if archivo_audio:
        grabacion.archivo_audio = archivo_audio
    grabacion.save()

    messages.success(request, "Grabación EDITADA exitosamente")
    return redirect('/grabacion/')
