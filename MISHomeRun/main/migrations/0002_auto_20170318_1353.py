# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20170315_2318'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='all_wp',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='bs_wp',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='coin',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='user',
            name='lp_wp',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='nlp_wp',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='team',
            field=models.ForeignKey(related_name='favor', to='team.Team', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='wdp_wp',
            field=models.IntegerField(null=True),
        ),
    ]
