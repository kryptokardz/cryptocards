# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-22 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='monster_story',
            field=models.TextField(default=''),
        ),
    ]
