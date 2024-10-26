from django.urls import path, include
from .views import *
app_name = 'favoritos'
urlpatterns = [
    path('', index_favoritos, name='index'),
    path('crear/', crear_favorito, name='crear'),
    path('borrar/<int:pk>', borrar_favorito, name="borrar"),
    path('detalle/<int:pk>', detalle_favorito, name="detalle"),
]