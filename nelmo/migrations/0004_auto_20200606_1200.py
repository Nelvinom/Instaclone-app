# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-06 09:00
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('nelmo', '0003_image_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=tinymce.models.HTMLField(),
        ),
    ]