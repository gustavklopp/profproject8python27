# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0009_auto_20140802_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='exoresult',
            name='discipline',
            field=models.ForeignKey(null=True, to='exercises.Discipline'),
            preserve_default=True,
        ),
    ]
