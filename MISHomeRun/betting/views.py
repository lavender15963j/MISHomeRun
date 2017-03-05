#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from betting.models import Betting
from customer.models import FakeNote
from main.mixins import PageTitleMixin
from betting.forms import FakeNoteForm

class PredictionView(PageTitleMixin, FormView):
    template_name = 'betting/prediction.html'
    page_title = '投注資訊'
    form_class = FakeNoteForm

    def get_context_data(self, **kwargs):
        ctx = super(PredictionView, self).get_context_data(**kwargs)
        ctx['bettings'] = Betting.objects.all().order_by('-game__date')
        return ctx

    def form_valid(self, form):
        self.lp = int(self.request.POST.get('lp'))
        self.nlp = int(self.request.POST.get('nlp'))
        self.bs = int(self.request.POST.get('bs'))
        self.wpd = int(self.request.POST.get('wpd'))

        betting_id = int(self.request.POST.get('betting'))
        betting = Betting.objects.get(id=betting_id)

        self.clearData(form)

        # FIXME: 需要做個檢察betting date是否結束

        if not FakeNote.objects.filter(user=self.request.user, betting=betting):
            fakeNote = FakeNote(
                user=self.request.user,
                betting=betting,
                lp_team=self.lp,
                nlp_team=self.nlp, 
                b_or_s=self.bs, 
                wpd_num=self.wpd, 
            )

            fakeNote.save()
            messages.success(self.request, "成功新增了一筆虛擬投注記錄")
        else:
            messages.warning(self.request, "您已投注過此筆記錄")

        return super(PredictionView, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "不成功")
        return super(PredictionView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('betting:prediction')

    def clearData(self, form):
        print self.lp, self.nlp, self.bs, self.wpd
        if self.lp not in [1, 0] or self.nlp not in [1, 0] or self.bs not in [1, 0]:
            return self.form_invalid(form)
        if self.wpd not in [1, 2, 3, 4, 5, 6, 7, 8, 9,]:
            return self.form_invalid(form)
        if self.lp == 1:
            self.lp = True
        else:
           self.lp = False
        if self.nlp == 1:
            self.nlp = True
        else:
            self.nlp = False
        if self.bs == 1:
            self.bs = True
        else:
            self.bs = False

        



