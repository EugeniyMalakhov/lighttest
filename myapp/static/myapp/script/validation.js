/**
 * Created by User on 03.02.2016.
 */


function validate() {
    if (document.getElementById('last_name').value==""){
        document.getElementById('error_last_name').innerHTML='Укажите вашу фамилию';
        return false;
    } else {
        document.getElementById('error_last_name').innerHTML="";
    }

    if (document.getElementById('first_name').value==""){
        document.getElementById('error_first_name').innerHTML='Укажите ваше имя';
        return false;
    } else {
        document.getElementById('error_first_name').innerHTML="";
    }

    if (document.getElementById('username').value==""){
        document.getElementById('error_username').innerHTML='Укажите логин';
        return false;
    } else {
        document.getElementById('error_username').innerHTML="";
    }

    if (document.getElementById('password1').value.length < 6 || document.getElementById('password1').value.length > 16){
        document.getElementById('error_password1').innerHTML='Пароль должен быть от 6 до 16 символов';
        return false;
    } else if (document.getElementById('password1').value != document.getElementById('password2').value){
        document.getElementById('error_password1').innerHTML="";
        document.getElementById('error_password2').innerHTML="Пароли не совпадают";
        return false;
    } else {
        document.getElementById('error_password2').innerHTML="";
    }

    if (document.getElementById('b_day').value==""){
        document.getElementById('error_b_day').innerHTML='Укажите дату рождения';
        return false;
    } else {
        document.getElementById('error_b_day').innerHTML="";
    }

    if (document.getElementById('email').value==""){
        document.getElementById('error_email').innerHTML='Укажите электронный адресс';
        return false;
    } else if (!document.getElementById('email').value.match(/^\w+\@\w+\.\w+$/ig)){
        document.getElementById('error_email').innerHTML="Укажите корректный адресс";
        return false;
    } else {
        document.getElementById('error_email').innerHTML="";
    }

    if (document.getElementById('phone').value==""){
        document.getElementById('error_phone').innerHTML='Укажите мобильный телефон';
        return false;
    } else if (document.getElementById('phone').value.match(/^\d{3}\-\d{7}$/)){
        document.getElementById('error_phone').innerHTML="Укажите в формате ***-*******";
        return false;
    } else {
        document.getElementById('error_phone').innerHTML="";
    }

    return true;
}