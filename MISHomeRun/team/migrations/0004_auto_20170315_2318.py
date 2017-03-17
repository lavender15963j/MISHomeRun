# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_team_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(height_field=b'height_field', width_field=b'width_field', null=True, upload_to=b'', blank=True),
        ),
    ]
