# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0002_auto_20170303_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betting',
            name='lp_away_team_odds',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='betting',
            name='lp_home_team_odds',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='betting',
            name='nlp_away_team_odds',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='betting',
            name='nlp_home_team_odds',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
    ]
