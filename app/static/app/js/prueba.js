//Formulario Nombres y apellido
const formulario_nom_ape = document.getElementById('Formulario_nom_ape');
const inputs_nom_ape = document.querySelectorAll('#Formulario_nom_ape input');

//Formularo Correo
const formulario_correo = document.getElementById('Formulario_Correo');
const inputs_correo = document.querySelectorAll('#Formulario_Correo input');

//Formulario Contraseñas
const formulario_contra = document.getElementById('Formulario_Contrasenas');
const inputs_contra = document.querySelectorAll('#Formulario_Contrasenas input');

const expresiones = {
	nombre: /^[a-zA-ZÀ-ÿ\s]{3,15}$/, // Letras y espacios, pueden llevar acentos.
	password: /^.{4,12}$/, // 4 a 12 digitos.
	correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/
}

const valirdarNombres = (e) =>{
    switch(e.target.name){
        case "name":
            if(expresiones.nombre.test(e.target.value)){
                document.querySelector('#divNombre .formulario__input-error').classList.remove('formulario__input-error-activo')
            } else {
                document.querySelector('#divNombre .formulario__input-error').classList.add('formulario__input-error-activo')
            }
        break;
        case "apel":
            if(expresiones.nombre.test(e.target.value)){
                document.querySelector('#divApellido .formulario__input-error').classList.remove('formulario__input-error-activo')
            } else {
                document.querySelector('#divApellido .formulario__input-error').classList.add('formulario__input-error-activo')
            }
        break;
    }
}

const validacionContra = (e) =>{
    const inputPassword1 = document.getElementById('pwd');
	const inputPassword2 = document.getElementById('pwdc');
    switch(e.target.name){
        case "pwd":
            if(expresiones.password.test(e.target.value)){
                document.querySelector('#divContra .formulario__input-error').classList.remove('formulario__input-error-activo')
            } else {
                document.querySelector('#divContra .formulario__input-error').classList.add('formulario__input-error-activo')
            }
        break;
        case "pwdc":
            if(inputPassword1.value !== inputPassword2.value){
                document.querySelector('#divContra2 .formulario__input-error').classList.add('formulario__input-error-activo')   
            } else {
                document.querySelector('#divContra2 .formulario__input-error').classList.remove('formulario__input-error-activo')
            }
        break;
    }
}

const valirdarEmail = (e) =>{
    
            if(expresiones.correo.test(e.target.value)){
                document.querySelector('#divEmail .formulario__input-error').classList.remove('formulario__input-error-activo')
            } else {
                document.querySelector('#divEmail .formulario__input-error').classList.add('formulario__input-error-activo')
            }

    }



inputs_contra.forEach((input) => {
    input.addEventListener('keyup',validacionContra);
    input.addEventListener('blur',validacionContra);
});

inputs_nom_ape.forEach((input) => {
    input.addEventListener('keyup',valirdarNombres);
    input.addEventListener('blur',valirdarNombres);
});

inputs_correo.forEach((input) => {
    input.addEventListener('keyup',valirdarEmail);
    input.addEventListener('blur',valirdarEmail);
});


