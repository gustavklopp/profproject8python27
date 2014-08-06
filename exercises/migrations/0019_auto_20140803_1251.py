# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0018_exercise_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='file',
            field=models.FileField(upload_to='exercises/static/', null=True),
        ),
    ]
