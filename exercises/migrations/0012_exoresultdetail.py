# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercises', '0011_auto_20140802_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExoResultDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('exo_number', models.IntegerField()),
                ('result_date', models.DateTimeField()),
                ('try_number', models.IntegerField(default='1')),
                ('truth', models.BooleanField(default=False)),
                ('discipline', models.ForeignKey(to='exercises.Discipline', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
