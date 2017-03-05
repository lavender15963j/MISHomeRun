# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='betting',
            name='away_team_odds',
        ),
        migrations.RemoveField(
            model_name='betting',
            name='home_team_odds',
        ),
        migrations.AddField(
            model_name='betting',
            name='lp_away_team_odds',
            field=models.DecimalField(default=1, max_digits=4, decimal_places=2),
        ),
        migrations.AddField(
            model_name='betting',
            name='lp_home_team_odds',
            field=models.DecimalField(default=1, max_digits=4, decimal_places=2),
        ),
        migrations.AddField(
            model_name='betting',
            name='nlp_away_team_odds',
            field=models.DecimalField(default=1, max_digits=4, decimal_places=2),
        ),
        migrations.AddField(
            model_name='betting',
            name='nlp_home_team_odds',
            field=models.DecimalField(default=1, max_digits=4, decimal_places=2),
        ),
    ]
