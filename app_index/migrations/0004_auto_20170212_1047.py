# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 10:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_index', '0003_auto_20170212_1012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='adress',
            new_name='address',
        ),
    ]