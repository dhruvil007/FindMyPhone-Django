# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-21 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='latitude',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='device',
            name='longitude',
            field=models.FloatField(default=1.0),
        ),
    ]
