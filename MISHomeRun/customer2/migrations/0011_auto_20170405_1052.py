# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer2', '0010_systemgiverecord_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemgiverecord',
            name='reason',
            field=models.TextField(null=True, blank=True),
        ),
    ]
