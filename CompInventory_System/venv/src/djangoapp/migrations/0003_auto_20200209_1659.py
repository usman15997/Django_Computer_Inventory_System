# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0002_auto_20200209_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='purchase_date',
            field=models.DateField(verbose_name='Purchase_date (mm/dd/yyyy)', blank=True),
        ),
    ]
