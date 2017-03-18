# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170318_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='all_wp',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='bs_wp',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='lp_wp',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nlp_wp',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='wdp_wp',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
