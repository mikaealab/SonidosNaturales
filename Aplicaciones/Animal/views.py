from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Animal

# Listar animales
def listaAnimales(request):
    animales = Animal.objects.all()
    return render(request, 'animal/lista.html', {'animales': animales})

# Mostrar formulario para nuevo animal
def nuevoAnimal(request):
    return render(request, "animal/nuevo.html")

# Guardar nuevo animal
def guardarAnimal(request):
    nombre_comun = request.POST["nombre_comun"]
    nombre_cientifico = request.POST["nombre_cientifico"]
    tipo = request.POST["tipo"]
    imagen = request.FILES.get("imagen", None)

    Animal.objects.create(
        nombre_comun=nombre_comun,
        nombre_cientifico=nombre_cientifico,
        tipo=tipo,
        imagen=imagen
    )

    messages.success(request, "Animal CREADO exitosamente")
    return redirect('/animal/')

# Eliminar animal
def eliminarAnimal(request, id):
    animal = Animal.objects.get(id=id)
    animal.delete()
    messages.success(request, "Animal ELIMINADO exitosamente")
    return redirect('/animal/')

# Mostrar formulario para editar
def editarAnimal(request, id):
    animalEditar = Animal.objects.get(id=id)
    return render(request, 'animal/editar.html', {'animalEditar': animalEditar})

# Procesar edición
def procesarEdicionAnimal(request):
    id = request.POST["id"]
    nombre_comun = request.POST["nombre_comun"]
    nombre_cientifico = request.POST["nombre_cientifico"]
    tipo = request.POST["tipo"]
    imagen = request.FILES.get("imagen", None)

    animal = Animal.objects.get(id=id)
    animal.nombre_comun = nombre_comun
    animal.nombre_cientifico = nombre_cientifico
    animal.tipo = tipo
    if imagen:
        animal.imagen = imagen
    animal.save()

    messages.success(request, "Animal EDITADO exitosamente")
    return redirect('/animal/')
