# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 18:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personinfo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='household',
        ),
    ]