# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='purchase_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 2, 9, 11, 49, 6, 798384, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='computer',
            name='timestamp',
            field=models.DateField(default=datetime.datetime(2020, 2, 9, 11, 49, 18, 227779, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
