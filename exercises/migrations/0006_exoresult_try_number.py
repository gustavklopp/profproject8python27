# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0005_auto_20140730_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='exoresult',
            name='try_number',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
