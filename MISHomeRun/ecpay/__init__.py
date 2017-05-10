#!/usr/bin/env python
# -*- coding: utf-8 -*-


import hashlib
import datetime

from django.conf import settings
from oscar.core.loading import get_class
from pyallpay import AllPay

from Iuppiter.Encoding import utf8

MERCHANT_TRADE_NO_LEN = 19

AIO_SANDBOX_SERVICE_URL = \
                    'https://payment-stage.ecpay.com.tw/Cashier/AioCheckOut/V2'
AIO_SERVICE_URL = 'https://payment.ecpay.com.tw/Cashier/AioCheckOut/V2'
    
def buildECPayForm(submission, scheme, domain):
    total = submission['order_total'].excl_tax
    basket = submission['basket']
    
    itemName = ''

    for index, line in enumerate(basket.all_lines()):
        product = line.product
        productName = product.get_title()
        itemName += utf8(productName)
        
        itemName += '%d元X%d#' % (line.price_excl_tax, line.quantity)
    
    itemName += "運費%d元X1" % submission['shipping_charge'].excl_tax
    
    
    basketId = basket.id
    
    tradeNo = 'BASKETID%d' % basketId
    
    
    hash = hashlib.sha224(str(datetime.datetime.now())).hexdigest().upper()
    lenNo = (MERCHANT_TRADE_NO_LEN - len(tradeNo))
    merchantTradeNo = str(hash[0:lenNo]) + tradeNo
     # Initialize the allPay config.
     
     
    ap = AllPay({'TotalAmount': int(total), 
                 'ChoosePayment': 'Credit', 
                 'MerchantTradeNo': merchantTradeNo, 
                 'ItemName': itemName,
                 'TradeDesc' : "Wonode T-shirt shop", 
                 'Remark' : 'Wonode',
                }
               )
    
    ap.service_url = \
      AIO_SANDBOX_SERVICE_URL if settings.ECPAY_SANDBOX else AIO_SERVICE_URL
    
    returnUrl = ap.url_dict['ReturnURL'].replace(
                           'localhost:8000', domain).replace('http', scheme)
    backUrl = ap.url_dict['OrderResultURL'].replace(
                           'localhost:8000', domain).replace('http', scheme)
    
    ap.url_dict['ReturnURL'] = returnUrl
    ap.url_dict['OrderResultURL'] = returnUrl
    ap.url_dict['ClientBackURL'] = backUrl
              
    dictUrl = ap.check_out()
    
    
    form = ap.gen_check_out_form(dictUrl, 
                                 settings.ALLPAY_AUTO_SEND_FORM)
                                      
    return form