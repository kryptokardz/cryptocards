# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-18 18:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_file', models.ImageField(upload_to='monsters_dir')),
                ('name', models.CharField(default='Laura', max_length=30)),
                ('health', models.IntegerField(default=3)),
                ('defense', models.IntegerField(default=7)),
                ('attack', models.IntegerField(default=3)),
                ('monster_type', models.CharField(default=('SLM', 'Slime'), max_length=100)),
                ('unique_id', models.CharField(default=-510043172199529891, max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monsters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]