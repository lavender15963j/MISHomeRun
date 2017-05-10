#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unicodedata
import urllib

from django.shortcuts import render
from django.views import generic
from django.template import RequestContext
from django.shortcuts import redirect, render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from oscar.core.loading import get_class, get_model
from django.views.generic import View
from django.template.context_processors import csrf
from django.conf import settings
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from models import ECPayTrade

from customer2.models import SystemGiveRecord

# allPay setting.
from pyallpay import AllPay

import logging
import json
import requests
import hashlib
import datetime


CheckoutSessionMixin = get_class('checkout.session', 'CheckoutSessionMixin')
PaymentDetailsView = get_class('checkout.views', 'PaymentDetailsView')

Source = get_model('payment', 'Source')
SourceType = get_model('payment', 'SourceType')
Basket = get_model('basket', 'Basket')

class SuccessResponseView(PaymentDetailsView):
    template_name_preview = 'allpay/preview.html'
    preview = True
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SuccessResponseView, self).dispatch(request, 
                                                         *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        ctx = {}
        return ctx
    
    def post(self, request, *args, **kwargs):
        # Posting to payment-details isn't the right thing to do.  Form
        # submissions should use the preview URL.
        
        self.tradeNo = request.POST.get('TradeNo')
        
        self.tradeAmt = request.POST.get('TradeAmt')
        
        self.merchantID = request.POST.get('MerchantID')
        self.merchantTradeNo = request.POST.get('MerchantTradeNo')
        self.rtnCode = request.POST.get('RtnCode')
        self.rtnMsg = request.POST.get('RtnMsg')
        self.payAmt = request.POST.get('MerchantID')
        self.tradeDate = request.POST.get('TradeDate')
        self.paymentType = request.POST.get('PaymentType')
        self.simulatePaid = request.POST.get('SimulatePaid')
        self.paymentDate = request.POST.get('PaymentDate')
        self.paymentTypeChargeFee = request.POST.get('PaymentTypeChargeFee')
        
        
        ecpayTrade = ECPayTrade.objects.create(
            tradeNo=self.tradeNo,
            tradeAmt=int(self.tradeAmt),
            merchantId=self.merchantID,
            merchantTradeNo=self.merchantTradeNo,
            rtnCode=self.rtnCode,
            payAmt=int(self.payAmt),
            tradeDate=self.tradeDate.replace('/', '-'),
            paymentType=self.paymentType,
            simulatePaid=self.simulatePaid,
            paymentDate=self.paymentDate.replace('/', '-'),
            paymentTypeChargeFee=self.paymentTypeChargeFee
        )
        ecpayTrade.save()
        
        
        index = request.POST.get('MerchantTradeNo').find('BASKETID')
        self.basketId = int(request.POST.get('MerchantTradeNo')[index + 8:])
        
        if not self.preview:
            return http.HttpResponseBadRequest()

        # We use a custom parameter to indicate if this is an attempt to place
        # an order (normally from the preview page).  Without this, we assume a
        # payment form is being submitted from the payment details view. In
        # this case, the form needs validating and the order preview shown.
        
        return self.handle_place_order_submission(request)
        
        
    def build_submission(self, **kwargs):
        submission = super(
            SuccessResponseView, self).build_submission(**kwargs)
        
        
        submission['payment_kwargs']['tradeNo'] = self.tradeNo
        submission['payment_kwargs']['tradeAmt'] = self.tradeAmt
        submission['payment_kwargs']['basketId'] = self.basketId
        return submission

    
    def handle_payment(self, order_number, total, **kwargs):
        tradeAmt = int(kwargs['tradeAmt'])
        tradeNo = kwargs['tradeNo']
        source_type, is_created = SourceType.objects.get_or_create(
            name='ECPay')
        source = Source(source_type=source_type,
                        currency='TWD',
                        amount_allocated=tradeAmt,
                        amount_debited=tradeAmt) 

        user = self.request.user
        coin = tradeAmt / 10
        record = SystemGiveRecord(
            receiver=user,
            note=None,
            give_coins=coin,
            reason="刷卡購買金幣%d枚" % coin,
        )
        record.save()
        user.coin = user.coin + coin
        user.save()

        
        self.add_payment_source(source)
        self.add_payment_event('Settled', tradeAmt,
                               reference=tradeNo)
                               
class TransactionListView(generic.ListView):
    model = ECPayTrade
    template_name = 'ecpay/TransactionList.html'
    context_object_name = 'transactions'
