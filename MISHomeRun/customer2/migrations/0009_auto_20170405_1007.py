# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer2', '0008_auto_20170318_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemgiverecord',
            name='w_bs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='systemgiverecord',
            name='w_lp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='systemgiverecord',
            name='w_nlp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='systemgiverecord',
            name='w_wpd',
            field=models.BooleanField(default=False),
        ),
    ]
