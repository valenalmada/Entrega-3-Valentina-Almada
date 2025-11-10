from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Universidad_de_Buenos_Aires

def inicio(request):
    return render(request, "inicio.html")

def otra(request):
    return render(request, "otra.html" )

def ingresar_uba(request, facultad, carrera):
    uba=Universidad_de_Buenos_Aires(facultad=facultad, carrera=carrera)
    uba.save()
    
    return render(request, "ingresar_uba.html", {"objeto_guardado": uba} )

def listar_info(request,):
    
    info_uba= Universidad_de_Buenos_Aires.objects.all()

    return render(request, "listar_info.html", {"listado_info_uba": info_uba})
