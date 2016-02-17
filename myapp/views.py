# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.core.context_processors import csrf

from myapp.forms import UserCreationForm, ChangeForm
from myapp.models import MyUser

# =========================== Главная страница (домашняя) Main page ==============================
def home(request):
    if request.user.is_authenticated():
        usr = get_object_or_404(MyUser, id=auth.get_user(request).id)
        args = {
            "username": auth.get_user(request).username,
            "usr": usr
        }
        return render(request, 'myapp/home.html', args)
    else:
        return render(request, 'myapp/home.html')


# =========================== Контакты contact ================================================
def contact(request):
    if request.user.is_authenticated():
        usr = get_object_or_404(MyUser, id=auth.get_user(request).id)
        args = {
            "username": auth.get_user(request).username,
            "usr": usr
        }
        return render(request, 'myapp/contact.html', args)
    else:
        return render(request, 'myapp/contact.html')


# =========================== Личный кабинет Office ==========================================
def office(request):
    if request.user.is_authenticated():
        usr = get_object_or_404(MyUser, id=auth.get_user(request).id)  # получаем пользователя который авторезировался
        form = ChangeForm(instance=request.user)
        args = {
            "form": form,
            "username": auth.get_user(request).username,
            "usr": usr
        }
        if request.POST:
            form = ChangeForm(request.POST or None, request.FILES or None, instance=request.user)
            if form.is_valid():
                form.save()
                usr = get_object_or_404(MyUser, id=auth.get_user(request).id)
                args = {
                    "form": form,
                    "username": auth.get_user(request).username,
                    "usr": usr
                }
                return render(request, 'myapp/office.html', args)
            else:
                args = {
                    "username": auth.get_user(request).username,
                    "usr": usr,
                    "form": form,
                    "login_error": "Заполните корректно",
                }
                return render(request, 'myapp/office.html', args)
        else:
            return render(request, 'myapp/office.html', args)
    else:
        return render(request, 'myapp/login.html')


# =========================== Логин Username ===================================================
def login(request):
    args = {}                                                          # словарь в котором хранятся параметры "в сессии"
    args.update(csrf(request))                                          # передаем параметр csrf - защита
    args['username'] = auth.get_user(request).username                  # добавляем в словарь username - пользователя
    if request.POST:                                                    # проверка на отправленные данные из формы
        username = request.POST.get('username', '')             # записываем в переменную username - имя пользователя
        password = request.POST.get('password', '')             # записываем в переменную password - пароль пользователя
        user = auth.authenticate(username=username, password=password)  # Авторизируем пользователя
        if user is not None:                                            # проверяем на пустые значения
            auth.login(request, user)                                   # сразу логеним пользователя
            usr = get_object_or_404(MyUser, id=auth.get_user(request).id)
            return redirect('/', usr)                                   # перебрасываем на начальную страницу
        else:                                                           # если переменные пустые то...
            args['login_error'] = "Пользователь не найден"              # в словарь добавляем ошибку
            return render(request, 'myapp/login.html', args)            # возвращаем пользователю форму логина
    else:                                                      # если параметры POST запроса небыли отправлены то...
        return render(request, 'myapp/login.html', args)                # Возвращаем пользователю форму логина


# ============================ Пароль Password ================================================
def logout(request):
    auth.logout(request)
    return redirect('/')

# ============================ Регистрация Registration ===========================================
def registr(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            user = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                     password=newuser_form.cleaned_data['password2'])
            auth.login(request, user)
            usr = get_object_or_404(MyUser, id=auth.get_user(request).id)
            return redirect('/', usr)
        else:
            args['login_error'] = "Заполните все поля"
            args['form'] = newuser_form
            return render(request, 'myapp/registr.html', args)
    return render(request, 'myapp/registr.html', args)

# ==============================  Удаление профайла Profile delete ================================

def delete(request):
    usr = get_object_or_404(MyUser, id=auth.get_user(request).id)
    usr.delete()
    return redirect('/')