# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='Логин')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Электронная почта')),
                ('b_day', models.DateField(blank=True, null=True, verbose_name='День рождения')),
                ('phone', models.CharField(max_length=15, unique=True, verbose_name='Телефон')),
                ('avatar', models.ImageField(blank=True, upload_to='images/%d', null=True, verbose_name='Аватар')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Админ')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'resume',
            },
        ),
    ]
