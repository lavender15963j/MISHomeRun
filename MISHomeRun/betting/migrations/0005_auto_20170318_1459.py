# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0004_auto_20170318_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='betting',
            name='a_odds1',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
        ),
        migrations.AddField(
            model_name='betting',
            name='a_odds2',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
        ),
        migrations.AddField(
            model_name='betting',
            name='a_odds3',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
        ),
        migrations.AddField(
            model_name='betting',
            name='a_odds4',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
        ),
        migrations.AddField(
            model_name='betting',
            name='a_odds5',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
        ),
        migrations.AddField(
            model_name='betting',
            name='a_odds6',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
        ),
        migrations.AddField(
            model_name='betting',
            name='a_odds7',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
        ),
        migrations.AddField(
            model_name='betting',
            name='a_odds8',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
        ),
        migrations.AddField(
            model_name='betting',
            name='a_odds9',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
        ),
    ]
