# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0015_exoresultdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='exoresultdetail',
            name='exo_number_detail',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
