# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0008_auto_20200211_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='export_to_CSV',
            field=models.BooleanField(default=False),
        ),
    ]
