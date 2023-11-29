from django.urls import path
from . import views  # Importa las vistas desde la misma aplicación

urlpatterns = [
    path('', views.informativa, name='informativa'),
    path('datos_contaminacion/', views.datos_contaminacion, name='datos_contaminacion'),
    path('descargar_app/', views.descargar_app, name='descargar_app'),
    path('heatmap/', views.heatmap_view, name='heatmap'),  # Agregada la URL para heatmap_view
]
