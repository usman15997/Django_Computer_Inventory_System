# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0005_auto_20200211_0457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operating_system',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('operating_system', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='computer',
            name='operating_system',
            field=models.ForeignKey(blank=True, null=True, to='djangoapp.Operating_system'),
        ),
    ]
