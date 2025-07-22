from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaAnimales, name='lista_animales'),
    path('nuevo/', views.nuevoAnimal, name='nuevo_animal'),
    path('guardar/', views.guardarAnimal, name='guardar_animal'),
    path('editar/<int:id>/', views.editarAnimal, name='editar_animal'),
    path('procesar/', views.procesarEdicionAnimal, name='procesar_edicion_animal'),
    path('eliminar/<int:id>/', views.eliminarAnimal, name='eliminar_animal'),
]
