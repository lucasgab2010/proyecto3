from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro
# Create your views here.

def inicio(resquest):
    return render(resquest, 'paginas/inicio.html')
def nosotros(resquest):
    return render(resquest, 'paginas/nosotros.html')

def libros(resquest):
    libros = libro.objects.all()   
    return render(resquest, 'libros/index.html')

def crear(resquest):
    return render(resquest, 'libros/crear.html')

def editar(resquest):
    return render(resquest, 'libros/editar.html')