# calidad_aire/views.py

from django.shortcuts import render
from django.http import Http404
from .models import DatosContaminacion
import folium
from folium import plugins
import json

def get_contamination_data():
    # Obtén datos de latitud y longitud desde el modelo Django DatosContaminacion
    return DatosContaminacion.objects.values('latitud', 'longitud', 'nivel_calor')

def calculate_center(data_points):
    # Calcula el centro de los datos
    if data_points:
        center_lat = sum(point['latitud'] for point in data_points) / len(data_points)
        center_lon = sum(point['longitud'] for point in data_points) / len(data_points)
        return center_lat, center_lon
    else:
        # Puedes establecer un centro predeterminado si no hay datos
        return 0, 0

def informativa(request):
    return render(request, 'informativa.html')

def datos_contaminacion(request):
    datos = DatosContaminacion.objects.all()
    return render(request, 'datos_contaminacion.html', {'datos': datos})

def descargar_app(request):
    return render(request, 'descargar_app.html')

def heatmap_view(request):
    try:
        # Obtén tus datos de latitud, longitud y nivel de calor desde tu modelo Django DatosContaminacion
        data_points = get_contamination_data()

        # Establece el centro en las coordenadas del Perú
        center_lat_peru, center_lon_peru = -9.1900, -75.0152

        # Crea un mapa Folium centrado en la ubicación específica o predeterminada
        my_map = folium.Map(location=[center_lat_peru, center_lon_peru], zoom_start=6)

        # Agrega un mapa de calor a Folium con franjas de colores
        heat_data = [[point['latitud'], point['longitud'], point['nivel_calor']] for point in data_points]
        plugins.HeatMap(heat_data, gradient={0.2: 'blue', 0.4: 'cyan', 0.6: 'lime', 0.8: 'yellow', 1: 'red'}).add_to(my_map)

        # Convierte los datos de calor a formato JSON
        heat_data_json = json.dumps(heat_data)

        # Convierte el mapa a HTML y pasa a la plantilla
        map_html = my_map._repr_html_()

        return render(request, 'heatmap.html', {'map_html': map_html, 'heat_data_json': heat_data_json})

    except DatosContaminacion.DoesNotExist:
        raise Http404("No hay datos de contaminación disponibles.")