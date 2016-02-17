# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.FileField(upload_to=myapp.models.get_upload_file_name, verbose_name='Аватар', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='b_day',
            field=models.DateField(verbose_name='Дата рождения', blank=True, null=True),
        ),
    ]
