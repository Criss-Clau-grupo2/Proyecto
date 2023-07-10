from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.inicio,name='index'), 
    path('nosotros/',views.nosotros,name='nosotros'),
    path('productos/',views.productos,name='productos'),
    path('vegano/',views.vegano,name='vegano'),
    path('pasteleria/',views.pasteleria,name='pasteleria'),
    path('panaderia/',views.panaderia,name='panaderia'),
    path('promociones/',views.promociones,name='promociones'),
    path('variedades/',views.variedades,name='variedades'),

    path('usuario/',include(('usuario.urls','usuario'))), 
    
    #CRUD DE PRODUCTO
    path('buscar',views.buscar,name='buscar'),
    path('agregarProducto',views.agregar_producto,name='agregar_producto'),
    path('borrarProducto/<str:pk>',views.eliminar_producto,name='productos_del'),
    path('buscarProductoAct/<str:pk>',views.buscar_producto,name='productos_findEdit'),
    path('actualizarProducto',views.actualizar_producto,name='actualizar_productos'),
    #CRUD CATEGORIA
    path('listaCategorias',views.listar_categoria,name='listar_categoria'), 
    path('agregarCategorias',views.agregar_categoria,name='agregar_categoria'),
    path('borrarCategorias/<str:pk>',views.eliminar_categoria,name='categoria_del'),
    path('actualizarCategorias/<str:pk>',views.modificar_categoria,name='categoria_edit'),
    #MENU USUARIO/ADMIN
    path('menuAdm',views.menu_admin,name='menu_adm'), 
    #MENU CARRITO
    path ('carrito/',views.tienda,name='tienda'),
    path ('agregar/<str:pk>',views.agregar_carrito,name='addcarrito'),
    path ('limpiar/',views.limpiar_carrito,name='limpcarrito'),
    
    
               
]

