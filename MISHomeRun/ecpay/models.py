#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.db import models

class ECPayTrade(models.Model):
    merchantId = models.CharField(max_length=30)
    merchantTradeNo = models.CharField(max_length=30)
    tradeNo = models.CharField(max_length=30)
    
    tradeDate = models.DateTimeField()
    paymentDate = models.DateTimeField()
    
    tradeAmt = models.IntegerField()
    payAmt = models.IntegerField()
         
    rtnCode = models.CharField(max_length=30)
    rtnMsg = models.CharField(max_length=30)
    paymentType = models.CharField(max_length=30)
    simulatePaid = models.CharField(max_length=30)
    paymentTypeChargeFee = models.CharField(max_length=30)
