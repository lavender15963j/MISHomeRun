# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Betting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('home_team_PN', models.BooleanField()),
                ('let_point_number', models.DecimalField(max_digits=4, decimal_places=2)),
                ('home_team_odds', models.DecimalField(max_digits=4, decimal_places=2)),
                ('away_team_odds', models.DecimalField(max_digits=4, decimal_places=2)),
                ('big_small_point_number', models.DecimalField(max_digits=4, decimal_places=2)),
                ('big_odds', models.DecimalField(max_digits=4, decimal_places=2)),
                ('small_odds', models.DecimalField(max_digits=4, decimal_places=2)),
                ('odds1', models.DecimalField(max_digits=4, decimal_places=2)),
                ('odds2', models.DecimalField(max_digits=4, decimal_places=2)),
                ('odds3', models.DecimalField(max_digits=4, decimal_places=2)),
                ('odds4', models.DecimalField(max_digits=4, decimal_places=2)),
                ('odds5', models.DecimalField(max_digits=4, decimal_places=2)),
                ('odds6', models.DecimalField(max_digits=4, decimal_places=2)),
                ('odds7', models.DecimalField(max_digits=4, decimal_places=2)),
                ('odds8', models.DecimalField(max_digits=4, decimal_places=2)),
                ('odds9', models.DecimalField(max_digits=4, decimal_places=2)),
                ('game', models.OneToOneField(to='game.Game')),
            ],
        ),
    ]
