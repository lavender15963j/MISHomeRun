# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemgiverecord',
            name='receiver',
            field=models.ForeignKey(related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='realnote',
            name='betting',
            field=models.ForeignKey(related_name='betting_real', to='betting.Betting'),
        ),
        migrations.AddField(
            model_name='realnote',
            name='user',
            field=models.ForeignKey(related_name='user_real', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='purchaserecord',
            name='buy_note',
            field=models.ForeignKey(related_name='buy_note', to='customer.FakeNote'),
        ),
        migrations.AddField(
            model_name='purchaserecord',
            name='buyer',
            field=models.ForeignKey(related_name='buyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fakenote',
            name='betting',
            field=models.ForeignKey(related_name='betting_fake', to='betting.Betting'),
        ),
        migrations.AddField(
            model_name='fakenote',
            name='user',
            field=models.ForeignKey(related_name='user_fake', to=settings.AUTH_USER_MODEL),
        ),
    ]
