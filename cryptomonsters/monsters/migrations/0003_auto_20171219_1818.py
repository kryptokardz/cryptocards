# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-19 18:18
from __future__ import unicode_literals

from django.db import migrations, models
import monsters.models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0002_auto_20171219_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='monster_type',
            field=models.CharField(default=monsters.models.random_type, max_length=100),
        ),
    ]