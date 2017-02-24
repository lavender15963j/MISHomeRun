# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20170217_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='game_data',
        ),
        migrations.AddField(
            model_name='gamedata',
            name='game',
            field=models.OneToOneField(null=True, blank=True, to='game.Game'),
        ),
    ]
