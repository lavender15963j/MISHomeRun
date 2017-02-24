# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20170218_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='wpd9',
            field=models.IntegerField(default=0),
        ),
    ]
