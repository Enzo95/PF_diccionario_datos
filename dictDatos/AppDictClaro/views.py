from django.shortcuts import render
from AppDictClaro.forms import *
from AppDictClaro.models import *
from django.views.generic import ListView, detail, edit
from django.urls import reverse_lazy



# Create your views here.
def inicio(request):

    return render(request,"AppDictClaro/inicio.html")

def tablas(request):

    return render(request,"AppDictClaro/tablas.html")

def buscar(request):

    return render(request,"AppDictClaro/buscar.html")

def acerca_info(request):

    return render(request,"AppDictClaro/acerca_de_nosotros.html")

def tablaFormulario(request):
    
    if request.method == "POST":

        miFormulario = TablaFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            tabla = Dicty(nombre=informacion['nombre'])
            tabla.save()

            return render(request, "AppDictClaro/inicio.html")
    
    else:
        miFormulario = TablaFormulario()

    return render(request,"AppDictClaro/tablaFormulario.html", {"miFormulario":miFormulario})

def tablacampoFormulario(request):
    
    if request.method == "POST":

        miFormulario = TablaCampoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            campo = Tabla(container=informacion['tabla'],campo=informacion['campo'],descripcion=informacion['descripcion'])
            campo.save()

            return render(request, "AppDictClaro/inicio.html")
    
    else:
        miFormulario = TablaCampoFormulario()

    return render(request,"AppDictClaro/tablacampoFormulario.html", {"miFormulario":miFormulario})


class TablaList(ListView):

    model = Dicty
    template_name= "AppDictClaro/tablas.html"

class TablasDetalle(detail.DetailView):

    model = Tabla
    template_name= "AppDictClaro/tablas_detalle.html"

class TablaCreacion(edit.CreateView):

    model = Dicty
    success_url= "/AppDictClaro/tablas/list"
    fields = ['nombre']

class TablaUpdate(edit.UpdateView):

    model = Tabla
    success_url= "/AppDictClaro/tablas/list"
    fields = ['campo','descripcion']

class TablaDelete(edit.DeleteView):

    model = Dicty
    success_url= "/AppDictClaro/tablas/list"