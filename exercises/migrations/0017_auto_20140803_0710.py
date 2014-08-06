# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0016_exoresultdetail_exo_number_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exoresult',
            name='result_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='exoresultdetail',
            name='result_date',
            field=models.DateTimeField(null=True),
        ),
    ]
