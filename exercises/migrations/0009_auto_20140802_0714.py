# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0008_auto_20140802_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exoresult',
            name='result_date',
            field=models.DateTimeField(),
        ),
    ]
