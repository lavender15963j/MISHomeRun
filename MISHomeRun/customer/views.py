#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views import generic
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from customer.models import Note
from customer.forms import NoteForm
from main.mixins import PageTitleMixin

class ProfileView(PageTitleMixin, generic.TemplateView):
    template_name = 'customer/profile.html'
    page_title = '個人資料'
    active_tab = 'profile'

    def get_context_data(self, **kwargs):
        ctx = super(ProfileView, self).get_context_data(**kwargs)
        return ctx

class RealNoteView(PageTitleMixin, CreateView):
    template_name = 'customer/real.html'
    page_title = '真實投注筆記'
    active_tab = 'real'
    form_class = NoteForm

    def get_success_url(self):
        messages.success(self.request, "成功新增了一筆筆記")
        return reverse_lazy('customer:real', kwargs={'pk': self.request.user.id, })

    def get_context_data(self, **kwargs):
        ctx = super(RealNoteView, self).get_context_data(**kwargs)
        ctx['notes'] = Note.objects.filter(user=self.request.user, note_type='real')
        return ctx
        

class FakeNoteView(PageTitleMixin, generic.TemplateView):
    template_name = 'customer/fake.html'
    page_title = '虛擬投注記錄'
    active_tab = 'fake'    
