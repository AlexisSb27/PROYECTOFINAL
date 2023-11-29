"""calidad_aire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from monitoreo.views import informativa, datos_contaminacion, descargar_app, heatmap_view

urlpatterns = [
    path('', informativa, name='informativa'),
    path('datos_contaminacion/', datos_contaminacion, name='datos_contaminacion'),
    path('descargar_app/', descargar_app, name='descargar_app'),
    path('heatmap/', heatmap_view, name='heatmap'),  # Agregada la URL para heatmap_view
]
