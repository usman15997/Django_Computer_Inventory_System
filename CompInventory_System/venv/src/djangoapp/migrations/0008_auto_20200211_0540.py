# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0007_auto_20200211_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='operating_system',
            field=models.CharField(max_length=30, blank=True, null=True, choices=[('Windows 10', 'Windows 10'), ('Windows 8', 'Windows 8'), ('Linux', 'Linux')]),
        ),
        migrations.DeleteModel(
            name='Operating_system',
        ),
    ]
