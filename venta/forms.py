from .models import Tipo_producto
from django.forms import ModelForm

class Tipo_productoForm(ModelForm):
    class Meta:
        model = Tipo_producto
        fields = ["desc_tipo_producto",]
        labels = {"desc_tipo_producto":"Categoria",}