# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20170111_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='couponcode',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
