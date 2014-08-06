# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0012_exoresultdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exoresult',
            name='result',
            field=models.IntegerField(default=0),
        ),
    ]
