# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-20 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20161219_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distrito',
            name='provincia',
        ),
        migrations.AddField(
            model_name='registro',
            name='me_entere',
            field=models.CharField(blank=True, choices=[('Facebook', 'Facebook'), ('Twiter', 'Twiter'), ('Amigo', 'Amigo'), ('publicidad calle', 'publicidad calle'), ('Otros', 'Otros')], max_length=60),
        ),
        migrations.DeleteModel(
            name='Distrito',
        ),
        migrations.DeleteModel(
            name='Provincia',
        ),
    ]