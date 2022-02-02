from django.urls import include, path

urlpatterns = [
    path('', include('cargar_archivo_rips.urls')),
    path('validaciones/', include('validaciones.urls')),
]
