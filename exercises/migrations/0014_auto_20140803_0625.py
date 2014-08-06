# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0013_auto_20140803_0619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exoresultdetail',
            name='discipline',
        ),
        migrations.RemoveField(
            model_name='exoresultdetail',
            name='user',
        ),
        migrations.DeleteModel(
            name='ExoResultDetail',
        ),
        migrations.AlterField(
            model_name='exoresult',
            name='result',
            field=models.IntegerField(),
        ),
    ]
