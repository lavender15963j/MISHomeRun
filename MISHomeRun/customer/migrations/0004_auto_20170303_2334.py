# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20170303_2038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fakenote',
            old_name='wpd1',
            new_name='wpd_num',
        ),
    ]
