# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from myapp.models import MyUser

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)
    b_day = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d'), input_formats=('%Y-%m-%d',))

    class Meta:
        model = MyUser
        fields = ['last_name',
                  'first_name',
                  'username',
                  'email',
                  'phone',
                  'b_day',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают!")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ['last_name',
                  'first_name',
                  'username',
                  'email',
                  'phone',
                  'b_day',
                  'avatar'
        ]

    def clean_password(self):
        return self.initial["password"]


class ChangeForm(forms.ModelForm):
    last_name = forms.TextInput(attrs={'required': False})
    last_name.render('last_name', 'Фамилия')

    b_day = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d'), input_formats=('%Y-%m-%d',))

    class Meta:
        model = MyUser
        fields = ['last_name',
                  'first_name',
                  'username',
                  'email',
                  'phone',
                  'b_day',
                  'avatar'
        ]

    def save(self, commit=True):
        user = super(ChangeForm, self).save(commit=False)
        user.last_name = self.cleaned_data['last_name']
        user.first_name = self.cleaned_data['first_name']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.b_day = self.cleaned_data['b_day']
        user.avatar = self.cleaned_data['avatar']

        if commit:
            user.save()

        return user

