# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-06-06 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0020_auto_20200527_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
