from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto,Tipo_producto
from .forms import Tipo_productoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group

# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR,"templates"),'
)

def inicio(request):
    listado_producto = Producto.objects.all().order_by('precio_producto','nombre_producto')
    listado_producto=listado_producto.filter(favorito_producto=1)
    context = {"producto":listado_producto}
    return render(request,'venta/index.html',context)
 
def nosotros(request):
    context = {}   
    return render(request,'venta/nosotros.html',context)

#listado para el cliente de todos los productos
def productos(request):
    listado_filtro = request.GET.get('filtro_productos')    
    listado_producto = Producto.objects.all().order_by('precio_producto','nombre_producto')
     
    if listado_filtro !='' and listado_filtro is not None:
        listado_producto=listado_producto.filter(nombre_producto__icontains=listado_filtro)    
        context = {"producto":listado_producto}
        return render(request,'venta/productos.html',context) 
    
    context = {"producto":listado_producto}         
    return render(request,'venta/productos.html',context)

#vista de pasteleria y filtro de productos
def pasteleria(request):
    listado_filtro = request.GET.get('filtro_pasteleria')    
    listado_producto = Producto.objects.all().order_by('precio_producto','nombre_producto')
    listado_producto=listado_producto.filter(id_tipo_producto=2)
     
    if listado_filtro !='' and listado_filtro is not None:
        listado_producto=listado_producto.filter(nombre_producto__icontains=listado_filtro)    
        context = {"producto":listado_producto}
        return render(request,'venta/pasteleria.html',context) 
    
    context = {"producto":listado_producto}         
    return render(request,'venta/pasteleria.html',context)

#vista panaderia y filtro de productos
def panaderia(request):
    listado_filtro = request.GET.get('filtro_panaderia')    
    listado_producto = Producto.objects.all().order_by('precio_producto','nombre_producto')
    listado_producto=listado_producto.filter(id_tipo_producto=3)
     
    if listado_filtro !='' and listado_filtro is not None:
        listado_producto=listado_producto.filter(nombre_producto__icontains=listado_filtro)    
        context = {"producto":listado_producto}
        return render(request,'venta/panaderia.html',context) 
    
    context = {"producto":listado_producto}         
    return render(request,'venta/panaderia.html',context)

#vista vegano y filtro de productos
def vegano(request):
    listado_filtro = request.GET.get('filtro_vegano')    
    listado_producto = Producto.objects.all().order_by('precio_producto','nombre_producto')
    listado_producto=listado_producto.filter(id_tipo_producto=5)
     
    if listado_filtro !='' and listado_filtro is not None:
        listado_producto=listado_producto.filter(nombre_producto__icontains=listado_filtro)    
        context = {"producto":listado_producto}
        return render(request,'venta/vegano.html',context) 
    
    context = {"producto":listado_producto}         
    return render(request,'venta/vegano.html',context)

#vista promociones y filtro de productos
def promociones(request):
    listado_filtro = request.GET.get('filtro_promociones')    
    listado_producto = Producto.objects.all().order_by('precio_producto','nombre_producto')
    listado_producto=listado_producto.filter(id_tipo_producto=9)
     
    if listado_filtro !='' and listado_filtro is not None:
        listado_producto=listado_producto.filter(nombre_producto__icontains=listado_filtro)    
        context = {"producto":listado_producto}
        return render(request,'venta/promociones.html',context) 
    
    context = {"producto":listado_producto}         
    return render(request,'venta/promociones.html',context)

#vista variedades
def variedades(request):
    context = {}   
    return render(request,'venta/variedades.html',context)

#prueba de buscar con filtro
@login_required
def buscar(request):    
    listado_filtro = request.GET.get('filtro')    
    listado_producto = Producto.objects.all().order_by('precio_producto','nombre_producto')
     
    if listado_filtro !='' and listado_filtro is not None:
        listado_producto=listado_producto.filter(nombre_producto__icontains=listado_filtro)    
        context = {"producto":listado_producto,"mensaje":"Lista de productos cargada CON FILTRO"}
        return render(request,'venta/buscar.html',context) 
    
    context = {"producto":listado_producto,"mensaje":"Lista de productos cargada SIN FILTRO"}
    return render(request,'venta/buscar.html',context) 

#prueba agregar producto
@login_required
def agregar_producto(request):
    if request.method !="POST":
        lista_tipo_productos = Tipo_producto.objects.all()
        context = {"tipo_productos":lista_tipo_productos}
        return render(request,'venta/producto_add.html',context)
    else:
        nombre_producto = request.POST["nombre_producto"]
        precio_producto = int(request.POST["precio_producto"])
        stock_producto = int(request.POST["stock_producto"])
        desc_producto = request.POST["desc_producto"]
        tipo_producto = request.POST["tipo_producto"]
        favorito_producto = 0
        imagen_producto = request.FILES["imagen_producto"]

        objTipo_producto = Tipo_producto.objects.get(id_tipo_producto=tipo_producto)

        objProducto = Producto.objects.create(
        
        nombre_producto = nombre_producto,
        precio_producto = precio_producto,
        stock_producto = stock_producto,
        desc_producto = desc_producto,
        favorito_producto = favorito_producto,
        imagen_producto = imagen_producto,
        id_tipo_producto = objTipo_producto
        )
        objProducto.save()
        lista_tipo_productos = Tipo_producto.objects.all()
        context = {"mensaje":"Se Agrego un nuevo producto en forma exitosa","tipo_productos":lista_tipo_productos}
        return render(request,'venta/producto_add.html',context)

#eliminar productos
@login_required
def eliminar_producto(request,pk):
    try:
        producto = Producto.objects.get(id_producto=pk) 
        producto.delete()
        lista_productos = Producto.objects.all().order_by('nombre_producto')
        context = {"mensaje":"Producto Eliminado","producto":lista_productos}
        return render(request,'venta/buscar.html',context)
    except:
        lista_productos = Producto.objects.all().order_by('nombre_producto')
        context = {"mensaje":"Error al Eliminar el Producto","producto":lista_productos}
        return render(request,'venta/buscar.html',context)

#buscar producto para modificarlo
@login_required
def buscar_producto(request,pk):
    if pk != "":
        producto = Producto.objects.get(id_producto=pk)
        lista_tipo_productos = Tipo_producto.objects.all()
        context = {"producto":producto,"tipo_productos":lista_tipo_productos}
        if producto:
            return render(request,'venta/producto_edit.html',context)
        else:
            context = {"mensaje":"Producto no existe"}
            return render(request,'venta/buscar.html',context)

#actualiza producto
@login_required
def actualizar_producto(request):
    if request.method == "POST":

        id_producto = request.POST["modificar_id_producto"]
        nombre_producto = request.POST["modificar_nombre_producto"]
        precio_producto = int(request.POST["modificar_precio_producto"])
        stock_producto = int(request.POST["modificar_stock_producto"])
        desc_producto = request.POST["modificar_desc_producto"]
        tipo_producto = request.POST["modificar_tipo_producto"]
        imagen_producto = request.FILES["modificar_imagen_producto"]
        favorito = request.POST["modificar_favorito"]

        objTipo_producto = Tipo_producto.objects.get(id_tipo_producto=tipo_producto)

        objProducto = Producto()
        objProducto.id_producto      = id_producto        
        objProducto.nombre_producto  = nombre_producto
        objProducto.precio_producto  = precio_producto
        objProducto.stock_producto   = stock_producto
        objProducto.desc_producto    = desc_producto
        objProducto.id_tipo_producto = objTipo_producto
        objProducto.imagen_producto = imagen_producto
        objProducto.favorito_producto = favorito
        objProducto.save()
        lista_tipo_productos = Tipo_producto.objects.all()
        context = {"mensaje":"Producto actualizado exitosamente","tipo_productos":lista_tipo_productos,"producto":objProducto}
        return render(request,'venta/producto_edit.html',context)
    else:
        lista_productos = Producto.objects.all().order_by('nombre_producto')
        context = {"productos":lista_productos}
        return render(request,'venta/producto_edit.html',context)
        #lista_tipo_productos = Tipo_producto.objects.all()
        #producto = Producto.objects.get(id_producto=pk)
        #context = {"producto":producto,"tipo_productos":lista_tipo_productos}
        #return render(request,'venta/producto_edit.html',context)

#listar categorias
@login_required
def listar_categoria(request):
    filtro_categoria = request.GET.get('filtro_categoria')
    lista_categorias = Tipo_producto.objects.all().order_by('desc_tipo_producto')
    
    if filtro_categoria != '' and filtro_categoria is not None:
        lista_categorias=lista_categorias.filter(desc_tipo_producto__startswith=filtro_categoria)    
        context = {"categoria":lista_categorias,"mensaje":"Lista de productos cargada CON FILTRO"}
        return render(request,'venta/categoria_list.html',context)
    
    context = {"mensaje":"Lista de Categorias cargada con exito","categoria":lista_categorias}
    return render(request,'venta/categoria_list.html',context)

#agregar categoria
@login_required
def agregar_categoria(request):
    if request.method =="POST":
        form = Tipo_productoForm(request.POST)
        if form.is_valid:
            form.save()
            form = Tipo_productoForm()
            context = {"mensaje":"Categoria agregada exitosamente","forms":form}
            return render(request,'venta/categoria_add.html',context)

    else:
        form = Tipo_productoForm()
        context = {"forms":form}
        return render(request,'venta/categoria_add.html',context)

#eliminar categoria
@login_required
def eliminar_categoria(request,pk):
    try:
        categoria = Tipo_producto.objects.get(id_tipo_producto=pk)
        if categoria:
            categoria.delete()
            lista_tipo_productos = Tipo_producto.objects.all().order_by('desc_tipo_producto')
            context = {"mensaje":"Categoria se ha eliminado correctamente","categoria":lista_tipo_productos}
            return render(request,'venta/categoria_list.html',context)

    except:
        lista_tipo_productos = Tipo_producto.objects.all().order_by('desc_tipo_producto')
        context = {"mensaje":"Error al eliminar la categoria","categoria":lista_tipo_productos}
        return render(request,'venta/categoria_list.html',context)       

#actualizar categorias
@login_required
def modificar_categoria(request,pk):
    try:
        categoria = Tipo_producto.objects.get(id_tipo_producto=pk)
        if categoria:
            if request.method == "POST":
                form = Tipo_productoForm(request.POST,instance=categoria)
                form.save()
                context = {"mensaje":"Se actualizo la Categoria","forms":form,"categorias":categoria}
                return render(request,'venta/categoria_edit.html',context)
            else:
                form = Tipo_productoForm(instance=categoria)
                context = {"mensaje":"","forms":form,"categorias":categoria}
                return render(request,'venta/categoria_edit.html',context)
    except:
        lista_categorias = Tipo_producto.objects.all().order_by('desc_tipo_producto')
        context = {"mensaje":"No existe la categoria","categoria":lista_categorias}
        return render(request,'venta/categoria_list.html',context)  

#menu admin

def menu_admin(request):          
    return render(request,'venta/menu_admin.html')       
 
#carrito
def tienda(request):
    productos = Producto.objects.all()
    return render(request,"venta/tienda.html", {'productos':productos}) 

#agrgar al carrito
def agregar_carrito(request,pk):
    carrito = productos(request) 
    producto = Producto.objects.get(id_producto=pk) 
    carrito.agregar_carrito(producto)
    return render(request,"venta/tienda.html")

#eliminar del carrito

def eliminar_del_carrito(request,id_producto):
    carrito = tienda(request) 
    producto = Producto.objects.get(id = id_producto) 
    carrito.eliminar(producto)
    return render(request,"venta/tienda.html")

def restar_producto(request,id_producto):
    carrito = tienda(request) 
    producto = Producto.objects.get(id = id_producto) 
    carrito.restar(producto)
    return render(request,"venta/tienda.html")

def limpiar_carrito(request):    
    carrito = tienda(request)
    carrito.limpiar()
    return render(request,"venta/tienda.html")
    
         
            
    
    
         
        
