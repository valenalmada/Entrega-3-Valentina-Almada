from django.urls import path
from django.urls import path
from inicio.views import inicio, otra, ingresar_uba, listar_info, ver_uba, ActualizarUba, EliminarUba

urlpatterns = [
    path("", inicio, name="Inicio"), 
    path("otra/", otra),
    path("ver-uba/<info_uba_id>", ver_uba, name="ver"),
    path("ingresar-uba/", ingresar_uba, name="Ingreso UBA"),
    path("listar-info/", listar_info, name="Carreras de Grado"),
    path("actualizar-uba/<pk>", ActualizarUba.as_view(), name="actualizar"),
    path("eliminar-uba/<pk>", EliminarUba.as_view(), name="eliminar")
    ]

    
    