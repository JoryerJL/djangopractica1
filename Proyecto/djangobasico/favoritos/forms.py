from django.forms import ModelForm
from .models import *


class FavoriteModelForm(ModelForm):
    class Meta:
        model = Favoritos
        fields = '__all__'