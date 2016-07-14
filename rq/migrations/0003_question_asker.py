# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 07:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rq', '0002_question_cdt'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='asker',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
