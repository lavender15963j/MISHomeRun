# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_auto_20170405_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemgiverecord',
            name='note',
            field=models.ForeignKey(related_name='by_note', to='customer.FakeNote', null=True),
        ),
    ]
