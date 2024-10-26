from distutils.command.config import config
from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def index_favoritos(request):
    favoritos_lista = Favoritos.objects.all()
    context = {
        'favoritos_lista': favoritos_lista
    }
    return render(request, 'favoritos/lista.html', context)


def crear_favorito(request):
    form = FavoriteModelForm()

    if request.method == 'POST':
        form = FavoriteModelForm(request.POST)
        if form.is_valid():
            form.save()
        else :
            print(form.errors)

    context = {
        'form': form,
        'titulo': 'Crear favorito',
    }
    return render(request, 'favoritos/crear.html', context)

def detalle_favorito(request, pk):
    favorito= Favoritos.objects.get(pk=pk)
    context = {
        'favorito': favorito
    }
    return render(request, 'favoritos/detalle.html', context )

def borrar_favorito(request, pk):
    Favoritos.objects.get(pk=pk).delete()
    return redirect('favoritos:index')

def actualizar_favorito(request, pk):
    favorito = Favoritos.objects.get(pk=pk)
    form = FavoriteModelForm(instance=favorito)

    if request.method == 'POST':
        form = FavoriteModelForm(request.POST, instance=favorito)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    context = {
        'form': form,
        'titulo': 'Actualizar favorito',
    }
    return render(request, 'favoritos/crear.html', context)
