# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20170217_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedata',
            name='game',
            field=models.OneToOneField(to='game.Game'),
        ),
    ]
