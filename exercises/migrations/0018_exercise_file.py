# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0017_auto_20140803_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='file',
            field=models.FileField(upload_to='static/', null=True),
            preserve_default=True,
        ),
    ]
