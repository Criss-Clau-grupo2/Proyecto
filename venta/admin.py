from django.contrib import admin
from .models import Tipo_producto,Producto,Usuario,Cliente,Boleta,Detalle_Boleta

# Register your models here.
admin.site.register(Tipo_producto)
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Boleta)
admin.site.register(Detalle_Boleta)