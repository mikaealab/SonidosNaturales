from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Aplicaciones.Animal.views import home  # <--- importa la vista home

urlpatterns = [
    path('', home, name='inicio'),  # ahora muestra home.html en la raíz
    path('admin/', admin.site.urls),

    path('animal/', include('Aplicaciones.Animal.urls')),
    path('ubicacion/', include('Aplicaciones.Ubicacion.urls')),
    path('grabacion/', include('Aplicaciones.Grabacion.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
