# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20170217_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_data',
            field=models.ForeignKey(blank=True, to='game.GameData', null=True),
        ),
    ]
