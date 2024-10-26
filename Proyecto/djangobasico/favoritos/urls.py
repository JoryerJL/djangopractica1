from django.urls import path, include
from .views import *
app_name = 'favoritos'
urlpatterns = [
    path('', index_favoritos),
    path('crear/', crear_favorito),
    path('borrar/<int:pk>', borrar_favorito, name="borrar"),
]