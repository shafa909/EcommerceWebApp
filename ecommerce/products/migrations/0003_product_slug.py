# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-24 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180723_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='abc'),
        ),
    ]
