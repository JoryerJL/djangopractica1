from django.db import models

# Create your models here.
class Favoritos(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
