# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20170315_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='image',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
