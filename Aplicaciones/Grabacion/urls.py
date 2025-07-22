from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaGrabaciones, name='lista_grabaciones'),
    path('nuevo/', views.nuevaGrabacion, name='nueva_grabacion'),
    path('guardar/', views.guardarGrabacion, name='guardar_grabacion'),
    path('editar/<int:id>/', views.editarGrabacion, name='editar_grabacion'),
    path('procesar/', views.procesarEdicionGrabacion, name='procesar_edicion_grabacion'),
    path('eliminar/<int:id>/', views.eliminarGrabacion, name='eliminar_grabacion'),
]
