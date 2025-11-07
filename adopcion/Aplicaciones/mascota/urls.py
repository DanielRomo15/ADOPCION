from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página principal al abrir '/'
    
    # PERSONA
    path('personas/', views.listar_personas, name='listar_personas'),
    path('personas/crear/', views.crear_persona, name='crear_persona'),
    path('personas/editar/<int:id>/', views.editar_persona, name='editar_persona'),
    path('personas/eliminar/<int:id>/', views.eliminar_persona, name='eliminar_persona'),

    # MASCOTA
    path('mascotas/', views.listar_mascotas, name='listar_mascotas'),
    path('mascotas/crear/', views.crear_mascota, name='crear_mascota'),
    path('mascotas/editar/<int:id>/', views.editar_mascota, name='editar_mascota'),
    path('mascotas/eliminar/<int:id>/', views.eliminar_mascota, name='eliminar_mascota'),

    # ADOPCION
    path('adopciones/', views.listar_adopciones, name='listar_adopciones'),
    path('adopciones/crear/', views.crear_adopcion, name='crear_adopcion'),
    path('adopciones/editar/<int:id>/', views.editar_adopcion, name='editar_adopcion'),
    path('adopciones/eliminar/<int:id>/', views.eliminar_adopcion, name='eliminar_adopcion'),

    path('adopciones/reportes/', views.reportes_adopciones, name='reportes_adopciones'),
    path('grafico/', views.grafico_adopciones, name='grafico_adopciones'),
]
