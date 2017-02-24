# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20170217_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_data',
            field=models.OneToOneField(null=True, blank=True, to='game.GameData'),
        ),
    ]
