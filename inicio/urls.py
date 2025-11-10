from django.urls import path
from django.urls import path
from inicio.views import inicio, otra, ingresar_uba, listar_info

urlpatterns = [
    path("", inicio), 
    path("otra/", otra),
    path("ingresar-uba/<facultad>/<carrera>/", ingresar_uba),
    path("listar-info/", listar_info)
    ]

    
    