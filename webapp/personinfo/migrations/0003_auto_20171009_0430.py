# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 04:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personinfo', '0002_remove_vehicle_household'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='household',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='personinfo.Household'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='personinfo.Person'),
        ),
    ]
