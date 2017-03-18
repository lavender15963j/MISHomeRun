# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20170318_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakenote',
            name='choice_team',
            field=models.BooleanField(),
        ),
    ]
