# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0002_auto_20170218_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bigsmallpoint',
            old_name='away_team_odds',
            new_name='big_odds',
        ),
        migrations.RenameField(
            model_name='bigsmallpoint',
            old_name='home_team_odds',
            new_name='small_odds',
        ),
    ]
