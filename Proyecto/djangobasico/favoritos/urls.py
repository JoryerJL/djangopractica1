from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index_favoritos),
    path('crear/', crear_favorito),
]