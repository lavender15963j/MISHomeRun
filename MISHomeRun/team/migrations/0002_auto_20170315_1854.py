# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='Coach',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='URL',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
