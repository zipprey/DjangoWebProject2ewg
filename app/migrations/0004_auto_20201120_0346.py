# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-20 00:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201118_0417'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.FileField(default='temp.jpg', upload_to='', verbose_name='Путь к картинке'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 20, 3, 46, 26, 443776), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 11, 20, 3, 46, 26, 443776), verbose_name='Дата'),
        ),
    ]
