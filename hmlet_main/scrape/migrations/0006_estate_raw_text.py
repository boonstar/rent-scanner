# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-19 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0005_estate_ask_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='raw_text',
            field=models.CharField(default='dummy', max_length=400),
            preserve_default=False,
        ),
    ]
