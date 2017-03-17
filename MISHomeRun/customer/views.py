#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views import generic
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from customer.models import RealNote, FakeNote
from main.models import User
from betting.models import Betting
from customer.forms import RealNoteForm, PurchaseForm
from main.mixins import PageTitleMixin

class ProfileView(PageTitleMixin, generic.TemplateView):
    template_name = 'customer/profile.html'
    page_title = '個人資料'
    active_tab = 'profile'

    def get_context_data(self, **kwargs):
        ctx = super(ProfileView, self).get_context_data(**kwargs)
        ctx['user'] = User.objects.get(username=kwargs.get('username'))
        return ctx

class RealNoteView(PageTitleMixin, FormView):
    template_name = 'customer/real.html'
    page_title = '真實投注筆記'
    active_tab = 'real'
    form_class = RealNoteForm

    def get_success_url(self):
        return reverse_lazy('customer:real', 
                            kwargs={'pk': self.request.user.id, })

    def form_valid(self, form):
        betting =  Betting.objects.get(id=self.request.POST.get('betting'))
        if not RealNote.objects.filter(user=self.request.user, betting=betting):
            messages.success(self.request, "成功新增了一筆筆記")
            
            realNote = form.save(commit=False)
            realNote.user = self.request.user
            realNote.betting = betting
            realNote.save()

        else:
            messages.warning(self.request, "您已新增過此賽事投注筆記")
        return super(RealNoteView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(RealNoteView, self).get_context_data(**kwargs)
        ctx['notes'] = RealNote.objects.filter(user=self.request.user)
        return ctx
        

class FakeNoteView(PageTitleMixin, generic.TemplateView):
    template_name = 'customer/fake.html'
    page_title = '虛擬投注記錄'
    active_tab = 'fake'

    def get_context_data(self, **kwargs):
        ctx = super(FakeNoteView, self).get_context_data(**kwargs)
        username = kwargs.get('username')
        ctx['user'] = User.objects.get(username=username)
        ctx['notes'] = FakeNote.objects.filter(
            user= ctx['user']).order_by('-betting__game__date')
        
        return ctx  
