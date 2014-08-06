# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30)),
                ('exo_number', models.IntegerField()),
                ('question', models.CharField(max_length=300)),
                ('question_type', models.CharField(max_length=30)),
                ('answer', models.CharField(max_length=30)),
                ('answer_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
