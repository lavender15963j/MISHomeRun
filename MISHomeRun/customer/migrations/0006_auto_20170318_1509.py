# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20170318_1341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realnote',
            old_name='wpd1',
            new_name='h_wpd1',
        ),
        migrations.RenameField(
            model_name='realnote',
            old_name='wpd2',
            new_name='h_wpd2',
        ),
        migrations.RenameField(
            model_name='realnote',
            old_name='wpd3',
            new_name='h_wpd3',
        ),
        migrations.RenameField(
            model_name='realnote',
            old_name='wpd4',
            new_name='h_wpd4',
        ),
        migrations.RenameField(
            model_name='realnote',
            old_name='wpd5',
            new_name='h_wpd5',
        ),
        migrations.RenameField(
            model_name='realnote',
            old_name='wpd6',
            new_name='h_wpd6',
        ),
        migrations.RenameField(
            model_name='realnote',
            old_name='wpd7',
            new_name='h_wpd7',
        ),
        migrations.RenameField(
            model_name='realnote',
            old_name='wpd8',
            new_name='h_wpd8',
        ),
        migrations.RenameField(
            model_name='realnote',
            old_name='wpd9',
            new_name='h_wpd9',
        ),
        migrations.AddField(
            model_name='fakenote',
            name='choice_team',
            field=models.NullBooleanField(),
        ),
    ]
