# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-06 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measure',
            name='low_is_good',
            field=models.NullBooleanField(),
        ),
    ]