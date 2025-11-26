from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Universidad_de_Buenos_Aires
from inicio.forms import IngresarUBA, BuscarCarrera
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, "inicio.html")

def otra(request):
    return render(request, "otra.html" )
@login_required
def ingresar_uba(request):
    if request.method=="POST":
        formulario=IngresarUBA(request.POST, request.FILES)
        if formulario.is_valid():
            info=formulario.cleaned_data

            uba=Universidad_de_Buenos_Aires(facultad=info.get("facultad"), carrera=info.get("carrera"), imagen=info.get("imagen"))
            uba.save()

            return redirect("Carreras de Grado")


            
    else:
        formulario=IngresarUBA()
    
    return render(request, "ingresar_uba.html", {"formulario":formulario} )

def listar_info(request,):
    
    formulario=BuscarCarrera(request.GET)
    if formulario.is_valid():
        carrera_a_buscar=formulario.cleaned_data.get("carrera")
        listado_carreras=Universidad_de_Buenos_Aires.objects.filter(carrera__icontains=carrera_a_buscar)

    return render(request, "listar_info.html", {"listado_info_uba": listado_carreras, "formulario":formulario})


def ver_uba(request, info_uba_id):

    info_uba= Universidad_de_Buenos_Aires.objects.get(id=info_uba_id)

    return render(request,"ver_uba.html", {"info_uba": info_uba})



class ActualizarUba(LoginRequiredMixin,UpdateView):
    model= Universidad_de_Buenos_Aires
    template_name= "actualizar_info.html"
    fields="__all__"
    success_url=reverse_lazy("Carreras de Grado")

class EliminarUba (LoginRequiredMixin,DeleteView):
    model= Universidad_de_Buenos_Aires
    template_name= "eliminar_info.html"
    success_url=reverse_lazy("Carreras de Grado")