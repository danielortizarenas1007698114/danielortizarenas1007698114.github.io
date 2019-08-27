from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy

from .models import Libro, Ejemplar

def cargar_inicio(request):
    return render(request, "miapp/index.html")

class LibroList(ListView):
    model = Libro
    template_name = 'miapp/lista_libros.html'


class LibroDetalle(DetailView):
    model = Libro
    template_name = 'miapp/detalle_libro.html'


class LibroCreate(CreateView):
    model = Libro
    fields = ['nombre','descripcion','isbn','copias']
    template_name = 'miapp/nuevo_libro.html'
    success_url = reverse_lazy('listar_libros')


class LibroUpdate(UpdateView):
    model = Libro
    fields = ['nombre','descripcion','isbn','copias']
    template_name = 'miapp/actualizar_libro.html'
    success_url = reverse_lazy('listar_libros')


class LibroDelete(DeleteView):
    model = Libro
    template_name = 'miapp/eliminar_libro.html'
    success_url = reverse_lazy('listar_libros')


class EjemplarLibro(ListView):
    model = Ejemplar
    template_name = 'miapp/ejemplar_libro.html'
#    success_url = reverse_lazy('listar_libros')


class EjemplarUpdate(UpdateView):
    model = Ejemplar
    template_name = 'miapp/editar_ejemplar.html'



class EjemplarCreate(CreateView):
    model = Ejemplar
    fields = ['numeroejemplar','fechadecompra','libro']
    template_name = 'miapp/nuevo_ejemplar.html'
    #success_url = reverse_lazy('listar_libros')

    