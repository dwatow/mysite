# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-08 02:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_remove_restaurant_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
