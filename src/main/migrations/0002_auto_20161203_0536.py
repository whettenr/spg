# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='insta_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='fb_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
