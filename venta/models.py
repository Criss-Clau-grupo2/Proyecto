from django.db import models

# Create your models here.

#dos primeras tablas son de los productos(tipo_producto,producto)
class Tipo_producto(models.Model):
    id_tipo_producto        = models.AutoField(db_column='idTipoProducto',primary_key=True)
    desc_tipo_producto      = models.CharField(max_length=20)

    def __str__(self):
        return str(self.desc_tipo_producto)

class Producto(models.Model):
    id_producto             = models.AutoField(db_column='idProducto',primary_key=True)
    nombre_producto         = models.CharField(max_length=40)
    precio_producto         = models.IntegerField()
    stock_producto          = models.IntegerField()
    desc_producto           = models.CharField(max_length=60)
    imagen_producto         = models.ImageField(upload_to='imagenes', null=True)
    favorito_producto       = models.IntegerField()
    id_tipo_producto        = models.ForeignKey('Tipo_producto',on_delete=models.CASCADE,db_column='id_tipo_producto')


    def __str__(self):
        return str(self.nombre_producto)+" $ "+str(self.precio_producto)

#dos primeras tablas de los usuarios(cliente, usuario)

class Usuario(models.Model):
    id_usuario              = models.AutoField(db_column='idUsuario',primary_key=True)
    nombre_usuario          = models.CharField(unique=True,max_length=16)
    contraseña              = models.CharField(max_length=16)

    def __str__(self):
        return str(self.nombre_usuario)+" / "+str(self.contraseña)

class Cliente(models.Model):
    id_cliente              = models.AutoField(db_column='idCliente',primary_key=True)  
    nombre_completo_cliente = models.CharField(max_length=60)
    telefono_cliente        = models.IntegerField()
    correo_cliente          = models.EmailField(unique=True,max_length=100)
    direccion_cliente       = models.CharField(max_length=100,blank=True,null=True)
    id_usuario              = models.ForeignKey('Usuario',on_delete=models.CASCADE,db_column='id_usuario')

    def __str__(self):
        return str(self.nombre_completo_cliente)+" / "+str(self.telefono_cliente)+" / "+str(self.correo_cliente)

#Tabla boleta y detalle de boleta

class Boleta(models.Model):
    id_boleta               = models.AutoField(db_column='idBoleta',primary_key=True)
    fecha_boleta            = models.DateField(blank=False,null=False) 
    id_cliente              = models.ForeignKey('Cliente',on_delete=models.CASCADE,db_column='id_cliente')

    def __str__(self):
        return str(self.id_boleta)+" / "+str(self.fecha_boleta)

class Detalle_Boleta(models.Model):
    id_detalle_boleta       = models.AutoField(db_column='idDetalleBoleta',primary_key=True)    
    id_boleta               = models.ForeignKey('Boleta',on_delete=models.CASCADE,db_column='id_boleta')
    id_producto             = models.ForeignKey('Producto',on_delete=models.CASCADE,db_column='id_producto')

    def __str__(self):
        return str(self.id_boleta)+" / "+str(self.id_producto)



