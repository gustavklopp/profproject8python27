# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0023_auto_20140803_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='question_type',
        ),
        migrations.AlterField(
            model_name='exercise',
            name='file',
            field=models.FileField(null=True, upload_to='exercises/static/exercises'),
        ),
    ]
