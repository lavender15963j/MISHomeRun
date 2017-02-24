# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='betting',
            field=models.ForeignKey(related_name='betting', to='betting.Betting'),
        ),
    ]
