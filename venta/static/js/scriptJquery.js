//EXPRESIONES REGULARES

var expr_correo = /^[a-zA-Z0-9_\.\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$/;
var expr_nombre = /^[a-zA-Z\s]+$/;
var expr_usuario1 = /^[a-zA-Z0-9_\$\!\¡\@\?\¿\=\;\:\.\-\$\%]+$/;
var expr_contacto = /^[0-9]+$/;
var expr_password1 = /^[a-zA-Z0-9_\$\!\¡\@\?\¿\=\;\:\.\-\$\%]+$/;

$(document).ready(function(){   
    
    //VALIDACION USUARIO
    $("#usuario1").keyup(function(e){
        
        var usuario1 = $("#usuario1").val(); 
        
        if(!expr_usuario1.test(usuario1)||usuario1.length < 4 ||usuario1.length > 16){         
            $("#texto_usuario1").show();                            
            $("#usuario1").css("border","3px solid #bb2929");  
        }else{
            $("#texto_usuario1").hide(); 
            $("#usuario1").css("border","3px solid #0075FF"); 
        }
    });

    $("#usuario1").blur(function(e){
        
        var usuario1 = $("#usuario1").val(); 
        
        if(usuario1 == ""){         
            $("#texto_usuario1").show();                            
            $("#usuario1").css("border","3px solid #bb2929");  
        }
    });
    
    //VALIDACION NOMBRE

    $("#nombre").keyup(function(e){
        
        var nombre = $("#nombre").val(); 
        
        if(!expr_nombre.test(nombre)||nombre.length < 3 ||nombre.length > 60){         
            $("#texto_nombre").show();                            
            $("#nombre").css("border","3px solid #bb2929");  
        }else{
            $("#texto_nombre").hide(); 
            $("#nombre").css("border","3px solid #0075FF"); 
        }
    });

    $("#nombre").blur(function(e){
        
        var nombre = $("#nombre").val(); 
        
        if(nombre == ""){         
            $("#texto_nombre").show();                            
            $("#nombre").css("border","3px solid #bb2929");  
        }
    });
    
    //VALIDACION CONTACTO

    $("#contacto").keyup(function(e){
        
        var contacto = $("#contacto").val(); 
        
        if(!expr_contacto.test(contacto)||contacto.length != 8){         
            $("#texto_contacto").show();                            
            $("#contacto").css("border","3px solid #bb2929");  
        }else{
            $("#texto_contacto").hide(); 
            $("#contacto").css("border","3px solid #0075FF"); 
        }
    });

    $("#contacto").blur(function(e){
        
        var contacto = $("#contacto").val(); 
        
        if(contacto == ""){         
            $("#texto_contacto").show();                            
            $("#contacto").css("border","3px solid #bb2929");  
        }
    });
    
    //VALIDACION CORREO

    $("#correo").keyup(function(e){
        
        var correo = $("#correo").val(); 
        
        if(!expr_correo.test(correo)){         
            $("#texto_correo").show();                            
            $("#correo").css("border","3px solid #bb2929");  
        }else{
            $("#texto_correo").hide(); 
            $("#correo").css("border","3px solid #0075FF"); 
        }
    });

    $("#correo").blur(function(e){
        
        var correo = $("#correo").val(); 
        
        if(correo == ""){         
            $("#texto_correo").show();                            
            $("#correo").css("border","3px solid #bb2929");  
        }
    });

    //VALIDACION CONTRASEÑA

    $("#password1").keyup(function(e){
        
        var password1 = $("#password1").val(); 
        
        if(!expr_password1.test(password1)||password1.length < 8 ||password1.length > 16){         
            $("#texto_password1").show();                            
            $("#password1").css("border","3px solid #bb2929");  
        }else{
            $("#texto_password1").hide(); 
            $("#password1").css("border","3px solid #0075FF"); 
        }
    });

    $("#password1").blur(function(e){
        
        var password1 = $("#password1").val(); 
        
        if(password1 == ""){         
            $("#texto_password1").show();                            
            $("#password1").css("border","3px solid #bb2929");  
        }
    });

    //VALIDACION REPETIR CONTRASEÑA    

    $("#password2").blur(function(e){
        
        var password1 = $("#password1").val();
        var password2 = $("#password2").val(); 
        
        if(password2 == ""|| password2 != password1){         
            $("#texto_password2").show();                            
            $("#password2").css("border","3px solid #bb2929");  
        }else{
            $("#texto_password2").hide(); 
            $("#password2").css("border","3px solid #0075FF"); 
        }
    });
    
    //VALIDACION BOTON SUMMIT

    $("#enviar").click(function(){
        
        var usuario1 = $("#usuario1").val();       
        var nombre = $("#nombre").val();
        var contacto = $("#contacto").val();
        var correo = $("#correo").val();
        var password1 = $("#password1").val();
        var password2 = $("#password2").val();
        var cbox = $("input[type = 'checkbox']:checked");     

        if(usuario1 == ""||!expr_usuario1.test(usuario1)||usuario1.length < 4 ||usuario1.length > 16){         
            $("#texto_usuario1").show();
            $("#usuario1").css("border","3px solid #bb2929");                              
            return false;
        }else{
            $("#texto_usuario1").hide(); 
            $("#usuario1").css("border","3px solid #0075FF");            
            if(nombre == ""||!expr_nombre.test(nombre)||nombre.length < 3 ||nombre.length > 60){
                $("#texto_nombre").show();
                $("#nombre").css("border","3px solid #bb2929"); 
                return false;
            }else{
                $("#texto_nombre").hide();
                $("#nombre").css("border","3px solid #0075FF"); 
                if(contacto == ""||!expr_contacto.test(contacto)||contacto.length != 8){
                    $("#texto_contacto").show();
                    $("#contacto").css("border","3px solid #bb2929"); 
                    return false;
                }else{
                    $("#texto_contacto").hide();
                    $("#contacto").css("border","3px solid #0075FF"); 
                    if(correo ==""||!expr_correo.test(correo)){
                        $("#texto_correo").show();
                        $("#correo").css("border","3px solid #bb2929"); 
                        return false;
                    }else{
                        $("#texto_correo").hide();
                        $("#correo").css("border","3px solid #0075FF"); 
                        if(password1 == ""||!expr_password1.test(password1)||password1.length < 8 ||password1.length > 16){
                            $("#texto_password1").show();
                            $("#password1").css("border","3px solid #bb2929"); 
                            return false;
                        }else{
                            $("#texto_password1").hide();
                            $("#password1").css("border","3px solid #0075FF"); 
                            if(password2 != password1){
                                $("#texto_password2").show();
                                $("#password2").css("border","3px solid #bb2929"); 
                                return false;                            
                            }else{
                                $("#texto_password2").hide();
                                $("#password2").css("border","3px solid #0075FF"); 
                                if(cbox.length == 0){
                                    $("#texto_checkbox").show();                                    
                                    return false;
                                }else{
                                    $("#texto_checkbox").hide();
                                    $("#formulario_exito").show();
                                    alert("Formulario enviado exitosamente");                                    
                                }; 
                            };
                        };
                    };
                };
            };
        };
        
    });    
});
