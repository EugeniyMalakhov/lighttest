# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from myapp.forms import UserChangeForm, UserCreationForm

from myapp.models import Resume, MyUser

admin.site.register(Resume)

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'last_name', 'first_name', 'email', 'b_day', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональные данные', {'fields': ('last_name', 'first_name', 'b_day', 'phone', 'avatar',)}),
        ('Статус', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('last_name', 'first_name', 'username', 'password1', 'password2', 'b_day', 'email', 'phone',)}
        ),
    )
    search_fields = ('username', 'email', 'phone',)
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(MyUser, UserAdmin)
admin.site.unregister(Group)

