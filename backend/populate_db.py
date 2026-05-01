import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from api.models import Negocio, Evento

Negocio.objects.all().delete()
Evento.objects.all().delete()

negocios_data = [
    {"nombre": "Restaurante Los Caciques", "categoria": "Restaurante", "direccion": "Cra. 5 #12-34", "telefono": "300 123 4567", "horario": "Lun-Dom: 11am-9pm", "lat": 9.2025, "lng": -73.5550},
    {"nombre": "Surti Mayorista", "categoria": "Supermercado", "direccion": "Calle 10 #6-15", "telefono": "301 987 6543", "horario": "Lun-Sab: 7am-8pm, Dom: 8am-2pm", "lat": 9.2040, "lng": -73.5535},
    {"nombre": "Tienda Black", "categoria": "Tienda local", "direccion": "Cra. 4 #9-20", "telefono": "320 456 7890", "horario": "Lun-Dom: 6am-10pm", "lat": 9.2010, "lng": -73.5560},
    {"nombre": "Panadería El Buen Trato", "categoria": "Panadería", "direccion": "Calle 11 #5-10", "telefono": "311 222 3344", "horario": "Lun-Dom: 5:30am-9pm", "lat": 9.2035, "lng": -73.5545},
    {"nombre": "Bancolombia", "categoria": "Banco", "direccion": "Cra. 6 #10-45", "telefono": "018000 912345", "horario": "Lun-Vie: 8am-11:30am, 2pm-4pm", "lat": 9.2018, "lng": -73.5530},
    {"nombre": "Droguería La Rebaja", "categoria": "Droguería", "direccion": "Calle 12 #4-50", "telefono": "300 999 8877", "horario": "24 Horas", "lat": 9.2020, "lng": -73.5570}
]

for item in negocios_data:
    Negocio.objects.create(**item)

eventos_data = [
    {"title": "Jornada de Embellecimiento Comunitario", "start": "2026-05-10T09:00:00Z", "color": "#005A8D"},
    {"title": "Taller de Alfabetización Digital UNAD", "start": "2026-05-15T09:00:00Z", "end": "2026-05-15T12:00:00Z", "color": "#F39200"},
    {"title": "Reunión de Seguridad Ciudadana", "start": "2026-05-18T18:00:00Z", "color": "#F4B533"},
    {"title": "Convocatoria Junta de Acción Comunal", "start": "2026-05-25T19:00:00Z", "color": "#005A8D"}
]

for item in eventos_data:
    Evento.objects.create(**item)

print("Base de datos poblada exitosamente.")
