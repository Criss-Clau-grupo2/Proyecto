$(document).ready(function(){
    $("#enviar").click(function(){
        $.get("https://api-klandeztino-default-rtdb.firebaseio.com/productos.json", 
            function(data){
                $.each(data, function(i,item){
                    $("#categorias").append("<tr><td>"+item.id+"</td><td>"+item.nombre+
                                    "</td><td>"+item.precio+
                                    "</td><td>"+item.descripcion+
                                    "</td><td><img src='"+item.imagen+"'></td></tr>");

                });

            });

    });

});


