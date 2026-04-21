from django.urls import path
from .views import listar_noticias, estatisticas

urlpatterns = [
    path('noticias/', listar_noticias),
    path('stats/', estatisticas),
]

from .views import listar_noticias, estatisticas, exportar_csv

urlpatterns = [
    path('noticias/', listar_noticias),
    path('stats/', estatisticas),
    path('export/csv/', exportar_csv),
]
