# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='cdt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
