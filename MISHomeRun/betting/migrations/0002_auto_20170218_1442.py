# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bigsmallpoint',
            name='away_team_odds',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='bigsmallpoint',
            name='big_small_point_number',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='bigsmallpoint',
            name='home_team_odds',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='letpoint',
            name='away_team_odds',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='letpoint',
            name='home_team_odds',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='letpoint',
            name='let_point_number',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='noletpoint',
            name='away_team_odds',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='noletpoint',
            name='home_team_odds',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='winpointdiff',
            name='odds1',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='winpointdiff',
            name='odds2',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='winpointdiff',
            name='odds3',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='winpointdiff',
            name='odds4',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='winpointdiff',
            name='odds5',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='winpointdiff',
            name='odds6',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='winpointdiff',
            name='odds7',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='winpointdiff',
            name='odds8',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='winpointdiff',
            name='odds9',
            field=models.DecimalField(max_digits=4, decimal_places=2),
        ),
    ]
