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
                ('winner', models.NullBooleanField()),
                ('away_team_score', models.IntegerField(null=True)),
                ('home_team_score', models.IntegerField(null=True)),
                ('away_team', models.ForeignKey(related_name='away_team', to='team.Team')),
                ('home_team', models.ForeignKey(related_name='home_team', to='team.Team')),
            ],
        ),
    ]
