# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercises', '0014_auto_20140803_0625'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExoResultDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exo_number', models.IntegerField()),
                ('result_date', models.DateTimeField()),
                ('try_number', models.IntegerField(default='1')),
                ('truth', models.BooleanField(default=False)),
                ('discipline', models.ForeignKey(null=True, to='exercises.Discipline')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
