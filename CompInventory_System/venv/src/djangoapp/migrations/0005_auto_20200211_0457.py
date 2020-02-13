# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0004_auto_20200211_0302'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='operating_system',
            field=models.CharField(max_length=30, blank=True, null=True, choices=[('Windows 10', 'Windows 10'), ('Windows 8', 'Windows 8'), ('Linux', 'Linux')]),
        ),
        migrations.AlterField(
            model_name='computer',
            name='IP_address',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='MAC_address',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='computer_name',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='location',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='users_name',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
