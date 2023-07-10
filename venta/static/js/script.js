
const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
    usuario: /^[a-zA-Z0-9]{4,16}$/,
    contraseña: /^[a-zA-Z0-9_\.\-\$\%]{8,16}$/
}

const campos = {
    usuario: false,
    password: false
}

const validaFormulario = (e) => {
    switch(e.target.name){
        case "usuario":
            validarCampo(expresiones.usuario, e.target, 'usuario');
        break;
        case "password":
            validarCampo(expresiones.contraseña, e.target, 'password');
        break;
    };
}

const validarCampo = (expresion, input, campo) => {
    if(expresion.test(input.value)){
        document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto');
        document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
        document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
        document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos[campo] = true;
    }else{
        document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto');
        document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
        document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
        document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
        campos[campo] = false;
    }
}

inputs.forEach((input) => {
    input.addEventListener('keyup', validaFormulario);
    input.addEventListener('blur', validaFormulario);            
});

formulario.addEventListener('submit', (e) => {
    e.preventDefault();
    if(campos.usuario && campos.password){
        alert("Formulario enviado con Exito!");
        formulario.reset();
        document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
        setTimeout(() => {
            document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo')
        }, 5000);
        document.querySelectorAll('.formulario__grupo-correcto').forEach((icono) => {
            icono.classList.remove('formulario__grupo-correcto');
        })
        document.getElementById('formulario__mensaje').classList.remove('formulario__mensaje-activo');    
    }else{       
        alert("Error en el formulario");
        document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
        setTimeout(() => {
            document.getElementById('formulario__mensaje').classList.remove('formulario__mensaje-activo')
        }, 5000);
    }
});

/*//usuario
function validar_user(){    
    
    var user,txt;
    
    user = document.getElementById("usuario").value;    
   
    if (user.length == 0){
        alert("Usuario Incorrecto");
        txt = "*El usuario tiene que ser de 4 a 16 digitos y solo puede contener numeros y letras";
        document.getElementById("usuario").focus();        
    }else{
        txt = "";
    }
    document.getElementById("valida_usuario").innerHTML = txt;      

}

 //contraseña
function validar_pass(){

    var pass,txt;

    pass = document.getElementById("password").value;

    if (pass.length < 8){
        alert("Contraseña Incorrecta");
        txt = "la contraseña debe tener minimo 8 y un maximo de 16 caracteres";
        document.getElementById("password").focus();
    }else{
        txt = "";
    }
    document.getElementById("valida_pass").innerHTML = txt;

}*/


