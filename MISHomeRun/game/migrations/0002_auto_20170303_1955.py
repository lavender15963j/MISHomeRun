# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='away_team_score',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='home_team_score',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
