# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20170218_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='Betting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('home_team_PN', models.CharField(max_length=5, choices=[(b'+', b'+'), (b'-', b'-')])),
                ('game', models.OneToOneField(to='game.Game')),
            ],
        ),
        migrations.CreateModel(
            name='BigSmallPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('big_small_point_number', models.DecimalField(max_digits=2, decimal_places=2)),
                ('home_team_odds', models.DecimalField(max_digits=2, decimal_places=2)),
                ('away_team_odds', models.DecimalField(max_digits=2, decimal_places=2)),
                ('betting', models.OneToOneField(to='betting.Betting')),
            ],
        ),
        migrations.CreateModel(
            name='LetPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('let_point_number', models.DecimalField(max_digits=2, decimal_places=2)),
                ('home_team_odds', models.DecimalField(max_digits=2, decimal_places=2)),
                ('away_team_odds', models.DecimalField(max_digits=2, decimal_places=2)),
                ('betting', models.OneToOneField(to='betting.Betting')),
            ],
        ),
        migrations.CreateModel(
            name='NoLetPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('home_team_odds', models.DecimalField(max_digits=2, decimal_places=2)),
                ('away_team_odds', models.DecimalField(max_digits=2, decimal_places=2)),
                ('betting', models.OneToOneField(to='betting.Betting')),
            ],
        ),
        migrations.CreateModel(
            name='WinPointDiff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('odds1', models.DecimalField(max_digits=2, decimal_places=2)),
                ('odds2', models.DecimalField(max_digits=2, decimal_places=2)),
                ('odds3', models.DecimalField(max_digits=2, decimal_places=2)),
                ('odds4', models.DecimalField(max_digits=2, decimal_places=2)),
                ('odds5', models.DecimalField(max_digits=2, decimal_places=2)),
                ('odds6', models.DecimalField(max_digits=2, decimal_places=2)),
                ('odds7', models.DecimalField(max_digits=2, decimal_places=2)),
                ('odds8', models.DecimalField(max_digits=2, decimal_places=2)),
                ('odds9', models.DecimalField(max_digits=2, decimal_places=2)),
                ('betting', models.OneToOneField(to='betting.Betting')),
            ],
        ),
    ]
