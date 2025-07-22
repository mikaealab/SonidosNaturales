from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: redirect('/animal/')),  # Redirect root URL to animal list
    path('admin/', admin.site.urls),
    path('animal/', include('Aplicaciones.Animal.urls')),
    path('ubicacion/', include('Aplicaciones.Ubicacion.urls')),
    path('grabacion/', include('Aplicaciones.Grabacion.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
