# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0006_exoresult_try_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exoresult',
            name='result',
            field=models.BooleanField(),
        ),
    ]
