# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-06 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nelmo', '0006_auto_20200606_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
