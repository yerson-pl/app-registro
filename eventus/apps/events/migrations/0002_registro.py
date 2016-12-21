# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-20 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('modificacion', models.DateField(auto_now=True)),
                ('nombre', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('celular', models.CharField(max_length=9)),
                ('organizacion', models.CharField(max_length=150)),
                ('ciudad', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Registros',
                'verbose_name': 'Registro',
            },
        ),
    ]
