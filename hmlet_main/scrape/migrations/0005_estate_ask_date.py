# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-19 06:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0004_estate_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='ask_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
