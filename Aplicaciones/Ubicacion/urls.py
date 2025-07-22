from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaUbicaciones, name='lista_ubicaciones'),
    path('nuevo/', views.nuevaUbicacion, name='nueva_ubicacion'),
    path('guardar/', views.guardarUbicacion, name='guardar_ubicacion'),
    path('editar/<int:id>/', views.editarUbicacion, name='editar_ubicacion'),
    path('procesar/', views.procesarEdicionUbicacion, name='procesar_edicion_ubicacion'),
    path('eliminar/<int:id>/', views.eliminarUbicacion, name='eliminar_ubicacion'),
]
