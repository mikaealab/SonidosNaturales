from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Ubicacion

# Listar
def listaUbicaciones(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'ubicacion/lista.html', {'ubicaciones': ubicaciones})

# Mostrar formulario nuevo
def nuevaUbicacion(request):
    return render(request, "ubicacion/nuevo.html")

# Guardar
def guardarUbicacion(request):
    nombre = request.POST["nombre"]
    latitud = request.POST["latitud"]
    longitud = request.POST["longitud"]
    descripcion = request.POST["descripcion"]

    Ubicacion.objects.create(
        nombre=nombre,
        latitud=latitud,
        longitud=longitud,
        descripcion=descripcion
    )

    messages.success(request, "Ubicación CREADA exitosamente")
    return redirect('/ubicacion/')

# Eliminar
def eliminarUbicacion(request, id):
    ubicacion = Ubicacion.objects.get(id=id)
    ubicacion.delete()
    messages.success(request, "Ubicación ELIMINADA exitosamente")
    return redirect('/ubicacion/')

# Mostrar formulario editar
def editarUbicacion(request, id):
    ubicacionEditar = Ubicacion.objects.get(id=id)
    return render(request, 'ubicacion/editar.html', {'ubicacionEditar': ubicacionEditar})

# Procesar edición
def procesarEdicionUbicacion(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    latitud = request.POST["latitud"]
    longitud = request.POST["longitud"]
    descripcion = request.POST["descripcion"]

    ubicacion = Ubicacion.objects.get(id=id)
    ubicacion.nombre = nombre
    ubicacion.latitud = latitud
    ubicacion.longitud = longitud
    ubicacion.descripcion = descripcion
    ubicacion.save()

    messages.success(request, "Ubicación EDITADA exitosamente")
    return redirect('/ubicacion/')
