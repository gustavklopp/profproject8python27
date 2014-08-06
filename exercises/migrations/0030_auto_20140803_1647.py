# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0029_auto_20140803_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='file',
            field=models.FileField(upload_to='static/exercises'),
        ),
    ]
