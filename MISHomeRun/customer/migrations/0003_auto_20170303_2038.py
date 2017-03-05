# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20170303_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakenote',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='purchaserecord',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='realnote',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='systemgiverecord',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
