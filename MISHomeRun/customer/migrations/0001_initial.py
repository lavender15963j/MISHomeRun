# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FakeNote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField()),
                ('lp_team', models.BooleanField()),
                ('nlp_team', models.BooleanField()),
                ('b_or_s', models.BooleanField()),
                ('wpd1', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('b_lp', models.BooleanField()),
                ('b_nlp', models.BooleanField()),
                ('b_bsp', models.BooleanField()),
                ('b_wpd', models.BooleanField()),
                ('create_date', models.DateTimeField()),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RealNote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField()),
                ('lp_home_team', models.IntegerField(default=0)),
                ('lp_away_team', models.IntegerField(default=0)),
                ('nlp_home_team', models.IntegerField(default=0)),
                ('nlp_away_team', models.IntegerField(default=0)),
                ('big', models.IntegerField(default=0)),
                ('small', models.IntegerField(default=0)),
                ('wpd1', models.IntegerField(default=0)),
                ('wpd2', models.IntegerField(default=0)),
                ('wpd3', models.IntegerField(default=0)),
                ('wpd4', models.IntegerField(default=0)),
                ('wpd5', models.IntegerField(default=0)),
                ('wpd6', models.IntegerField(default=0)),
                ('wpd7', models.IntegerField(default=0)),
                ('wpd8', models.IntegerField(default=0)),
                ('wpd9', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SystemGiveRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField()),
                ('give_coins', models.IntegerField()),
                ('reason', models.TextField(blank=True)),
            ],
        ),
    ]
