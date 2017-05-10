# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ECPayTrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('merchantId', models.CharField(max_length=30)),
                ('merchantTradeNo', models.CharField(max_length=30)),
                ('tradeNo', models.CharField(max_length=30)),
                ('tradeDate', models.DateTimeField()),
                ('paymentDate', models.DateTimeField()),
                ('tradeAmt', models.IntegerField()),
                ('payAmt', models.IntegerField()),
                ('rtnCode', models.CharField(max_length=30)),
                ('rtnMsg', models.CharField(max_length=30)),
                ('paymentType', models.CharField(max_length=30)),
                ('simulatePaid', models.CharField(max_length=30)),
                ('paymentTypeChargeFee', models.CharField(max_length=30)),
            ],
        ),
    ]
