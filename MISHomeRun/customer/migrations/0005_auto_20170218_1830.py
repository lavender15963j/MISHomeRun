# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_note_wpd9'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='b_home_team',
            new_name='big',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='s_away_team',
            new_name='small',
        ),
    ]
