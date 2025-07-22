from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static  # ✅ IMPORTANTE
from Aplicaciones.Animal.views import home 

urlpatterns = [
    path('', home, name='inicio'),
    path('admin/', admin.site.urls),
    path('animal/', include('Aplicaciones.Animal.urls')),
    path('ubicacion/', include('Aplicaciones.Ubicacion.urls')),
    path('grabacion/', include('Aplicaciones.Grabacion.urls')),
]

# ✅ ESTA PARTE ES CRUCIAL PARA SERVIR /media/ EN MODO DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
