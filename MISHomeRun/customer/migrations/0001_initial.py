# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('team', '0002_auto_20170217_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note_type', models.CharField(max_length=5, choices=[(b'fake', b'Fake'), (b'real', b'Real')])),
                ('lp_home_team', models.IntegerField()),
                ('lp_away_team', models.IntegerField()),
                ('nlp_home_team', models.IntegerField()),
                ('nlp_away_team', models.IntegerField()),
                ('b_home_team', models.IntegerField()),
                ('s_away_team', models.IntegerField()),
                ('wpd1', models.IntegerField()),
                ('wpd2', models.IntegerField()),
                ('wpd3', models.IntegerField()),
                ('wpd4', models.IntegerField()),
                ('wpd5', models.IntegerField()),
                ('wpd6', models.IntegerField()),
                ('wpd7', models.IntegerField()),
                ('wpd8', models.IntegerField()),
                ('betting', models.ForeignKey(related_name='betting', to='team.Team')),
                ('user', models.ForeignKey(related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
