from distutils.command.config import config
from lib2to3.fixes.fix_input import context

from django.shortcuts import render
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
        'form': form
    }
    return render(request, 'favoritos/crear.html', context)