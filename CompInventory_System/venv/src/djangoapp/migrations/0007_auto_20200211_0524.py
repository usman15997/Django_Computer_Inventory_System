# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0006_auto_20200211_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='operating_system',
            field=models.ForeignKey(null=True, to='djangoapp.Operating_system'),
        ),
    ]
