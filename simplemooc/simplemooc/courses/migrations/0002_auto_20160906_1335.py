# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses/img', verbose_name='Imagem'),
        ),
    ]
