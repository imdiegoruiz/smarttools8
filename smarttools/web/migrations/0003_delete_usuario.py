# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 07:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_competition_video'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
