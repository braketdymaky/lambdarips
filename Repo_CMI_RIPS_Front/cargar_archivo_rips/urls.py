from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cargar-archivo-rips/', views.cargar_archivo_rips, name='cargar-archivo-rips'),
    path('validar-datos-rips/', views.validar_datos_rips, name='validar-datos-rips'),
    path('guardar-datos-rips/', views.guardar_datos_rips, name='guardar-datos-rips')
]
