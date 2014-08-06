# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0022_auto_20140803_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='file',
            field=models.FileField(upload_to='', null=True),
        ),
    ]
