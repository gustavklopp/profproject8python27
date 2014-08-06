# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0003_auto_20140730_0928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='subject',
            new_name='discipline',
        ),
    ]
