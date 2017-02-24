# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20170218_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='b_home_team',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='note',
            name='lp_away_team',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='note',
            name='lp_home_team',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='note',
            name='nlp_away_team',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='note',
            name='nlp_home_team',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='note',
            name='s_away_team',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='note',
            name='wpd1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='note',
            name='wpd2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='note',
            name='wpd3',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='note',
            name='wpd4',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='note',
            name='wpd5',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='note',
            name='wpd6',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='note',
            name='wpd7',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='note',
            name='wpd8',
            field=models.IntegerField(default=0),
        ),
    ]
