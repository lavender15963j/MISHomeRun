#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oscar.core.loading import get_class

from ecpay import buildECPayForm
_PaymentDetailsView = get_class('checkout.views', 'PaymentDetailsView')

class PaymentDetailsView(_PaymentDetailsView):
    def dispatch(self, request, *args, **kwargs):
        
        self.scheme = request.scheme
        self.domain = request.META['HTTP_HOST']
        return super(PaymentDetailsView, self).dispatch(
            request, *args, **kwargs)
            
    def get_context_data(self, **kwargs):
        kwargs = super(PaymentDetailsView, self).get_context_data(**kwargs)
        
        submission = self.build_submission()
        
        form = buildECPayForm(submission, self.scheme, self.domain)
        
        kwargs['form'] = form
        
        return kwargs