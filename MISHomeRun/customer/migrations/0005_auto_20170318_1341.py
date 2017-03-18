# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20170303_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaserecord',
            name='b_bsp',
        ),
        migrations.RemoveField(
            model_name='purchaserecord',
            name='b_lp',
        ),
        migrations.RemoveField(
            model_name='purchaserecord',
            name='b_nlp',
        ),
        migrations.RemoveField(
            model_name='purchaserecord',
            name='b_wpd',
        ),
        migrations.AddField(
            model_name='purchaserecord',
            name='buy_for',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
