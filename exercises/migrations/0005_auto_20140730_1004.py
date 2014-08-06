# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0004_auto_20140730_0950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='answer_date',
            new_name='question_date',
        ),
    ]
