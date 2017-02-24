# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('game_no', models.IntegerField()),
                ('stadium', models.CharField(max_length=10)),
                ('date', models.DateTimeField()),
                ('away_team', models.ForeignKey(related_name='away_team', to='team.Team')),
            ],
        ),
        migrations.CreateModel(
            name='GameData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('away_team_score', models.IntegerField()),
                ('home_team_score', models.IntegerField()),
                ('winner', models.ForeignKey(to='team.Team')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='game_data',
            field=models.ForeignKey(to='game.GameData'),
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(related_name='home_team', to='team.Team'),
        ),
    ]
