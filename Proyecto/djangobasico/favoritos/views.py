from distutils.command.config import config
from django.shortcuts import render
from .forms import *

# Create your views here.
def index_favoritos(request):
    return render(request, 'index.html')


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