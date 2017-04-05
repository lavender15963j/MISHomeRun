# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20170315_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(default=0, max_length=10)),
                ('year', models.IntegerField(max_length=10)),
                ('Team_1_G', models.IntegerField(default=0, null=True, blank=True)),
                ('Team_1_W', models.IntegerField(default=0, null=True, blank=True)),
                ('Team_1_L', models.IntegerField(default=0, null=True, blank=True)),
                ('Team_1_T', models.IntegerField(default=0, null=True, blank=True)),
                ('Team_1_PCT', models.FloatField(default=0, null=True, blank=True)),
                ('Team_1_Whome', models.IntegerField(default=0, null=True, blank=True)),
                ('Team_1_Lhome', models.IntegerField(default=0, null=True, blank=True)),
                ('Team_1_Thome', models.IntegerField(default=0, null=True, blank=True)),
                ('Team_1_Waway', models.IntegerField(default=0, null=True, blank=True)),
                ('Team_1_Laway', models.IntegerField(default=0, null=True, blank=True)),
                ('Team_1_Taway', models.IntegerField(default=0, null=True, blank=True)),
                ('Team_2_G', models.IntegerField(default=0, null=True, blank=True)),
                ('Team_2_W', models.IntegerField(default=0, null=True, blank=True)),
                ('Team_2_L', models.IntegerField(default=0, null=True, blank=True)),
                ('Team_2_T', models.IntegerField(default=0, null=True, blank=True)),
                ('Team_2_PCT', models.FloatField(default=0, null=True, blank=True)),
                ('Team_2_Whome', models.IntegerField(default=0, null=True, blank=True)),
                ('Team_2_Lhome', models.IntegerField(default=0, null=True, blank=True)),
                ('Team_2_Thome', models.IntegerField(default=0, null=True, blank=True)),
                ('Team_2_Waway', models.IntegerField(default=0, null=True, blank=True)),
                ('Team_2_Laway', models.IntegerField(default=0, null=True, blank=True)),
                ('Team_2_Taway', models.IntegerField(default=0, null=True, blank=True)),
                ('Pitch_ERA', models.FloatField(default=0, null=True, blank=True)),
                ('Pitch_IP', models.FloatField(default=0, null=True, blank=True)),
                ('Pitch_BF', models.IntegerField(default=0, null=True, blank=True)),
                ('Pitch_H', models.IntegerField(default=0, null=True, blank=True)),
                ('Pitch_HR', models.IntegerField(default=0, null=True, blank=True)),
                ('Pitch_SO', models.IntegerField(default=0, null=True, blank=True)),
                ('Pitch_WP', models.IntegerField(default=0, null=True, blank=True)),
                ('Pitch_BK', models.IntegerField(default=0, null=True, blank=True)),
                ('Pitch_R', models.IntegerField(default=0, null=True, blank=True)),
                ('Pitch_ER', models.IntegerField(default=0, null=True, blank=True)),
                ('Hit_AVG', models.FloatField(default=0, null=True, blank=True)),
                ('Hit_G', models.IntegerField(default=0, null=True, blank=True)),
                ('Hit_AB', models.IntegerField(default=0, null=True, blank=True)),
                ('Hit_R', models.IntegerField(default=0, null=True, blank=True)),
                ('Hit_RBI', models.IntegerField(default=0, null=True, blank=True)),
                ('Hit_H', models.IntegerField(default=0, null=True, blank=True)),
                ('Hit_HR', models.IntegerField(default=0, null=True, blank=True)),
                ('Hit_SAC', models.IntegerField(default=0, null=True, blank=True)),
                ('Hit_SO', models.IntegerField(default=0, null=True, blank=True)),
                ('Hit_SB', models.IntegerField(default=0, null=True, blank=True)),
                ('Hit_OBP', models.FloatField(default=0, null=True, blank=True)),
                ('Hit_SLG', models.FloatField(default=0, null=True, blank=True)),
                ('Defense_FPCT', models.FloatField(default=0, null=True, blank=True)),
                ('Defense_TC', models.IntegerField(default=0, null=True, blank=True)),
                ('Defense_PO', models.IntegerField(default=0, null=True, blank=True)),
                ('Defense_A', models.IntegerField(default=0, null=True, blank=True)),
                ('Defense_DP', models.IntegerField(default=0, null=True, blank=True)),
                ('Defense_E', models.IntegerField(default=0, null=True, blank=True)),
                ('Defense_CS', models.IntegerField(default=0, null=True, blank=True)),
                ('Defense_PB', models.IntegerField(default=0, null=True, blank=True)),
                ('name', models.ForeignKey(to='team.Team')),
            ],
        ),
    ]
