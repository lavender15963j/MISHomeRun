#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from betting.models import Betting
from customer.models import FakeNote
from main.mixins import PageTitleMixin
from betting.forms import FakeNoteForm

class PredictionView(PageTitleMixin, FormView):
    template_name = 'betting/prediction.html'
    page_title = '投注資訊'
    form_class = FakeNoteForm
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PredictionView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(PredictionView, self).get_context_data(**kwargs)
        ctx['bettings'] = Betting.objects.all().order_by('-game__date')
        return ctx

    def form_valid(self, form):
        self.lp = int(self.request.POST.get('lp'))
        self.nlp = int(self.request.POST.get('nlp'))
        self.bs = int(self.request.POST.get('bs'))
        self.wpd = int(self.request.POST.get('wpd'))
        self.choice = int(self.request.POST.get('choice'))

        betting_id = int(self.request.POST.get('betting'))
        betting = Betting.objects.get(id=betting_id)
        
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
        if self.choice == 1:
            self.choice = True
        else:
            self.choice = False
        # FIXME: 需要做個檢察betting date是否結束

        if not FakeNote.objects.filter(user=self.request.user, betting=betting):
            coin = self.request.user.coin
            cost = 4
            if coin - cost >= 0:
                fakeNote = FakeNote(
                    user=self.request.user,
                    betting=betting,
                    lp_team=self.lp,
                    nlp_team=self.nlp, 
                    b_or_s=self.bs,
                    choice_team=self.choice,
                    wpd_num=self.wpd, 
                )
                self.request.user.coin = coin - cost
                self.request.user.save()
                
                fakeNote.save()
                messages.success(self.request, "成功投注No.%d，花費%d枚金幣，剩餘%d枚金幣" % (betting.game.game_no, cost, self.request.user.coin))
            else:
                messages.warning(self.request, "金幣不足，您只剩下%d枚金幣" % coin)
        else:
            messages.warning(self.request, "您已投注過此筆記錄")

        return super(PredictionView, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "不成功，所有欄位都必須填寫")
        return super(PredictionView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('betting:prediction')


class BettingDetailView(PageTitleMixin, generic.detail.DetailView):
    template_name = 'betting/bettingdetail.html'
    page_title = '投注情形'
    context_object_name = 'betting'

    def get(self, request, *args, **kwargs):
        self.betting_id = kwargs.get('pk')
        return super(BettingDetailView, self).get(request, *args, **kwargs)

    def get_object(self):
        self.betting = Betting.objects.get(id=self.betting_id)
        return self.betting

    def get_context_data(self, **kwargs):
        ctx = super(BettingDetailView, self).get_context_data(**kwargs)
        notes = FakeNote.objects.filter(betting=self.betting)
        ctx['num'] = len(notes)

        # lp
        ctx['h_lp'] = 0
        ctx['a_lp'] = 0
        ctx['h_lp_p'] = 0
        ctx['a_lp_p'] = 0

        # nlp
        ctx['h_nlp'] = 0
        ctx['a_nlp'] = 0
        ctx['h_nlp_p'] = 0
        ctx['a_nlp_p'] = 0

        # bs
        ctx['b'] = 0
        ctx['s'] = 0
        ctx['b_p'] = 0
        ctx['s_p'] = 0

        # wdp
        ctx['h_wdp'] = [0, 0, 0, 0, 0, 0, 0, 0, 0,]
        ctx['a_wdp'] = [0, 0, 0, 0, 0, 0, 0, 0, 0,]
        ctx['h_wdp_p'] = [0, 0, 0, 0, 0, 0, 0, 0, 0,]
        ctx['a_wdp_p'] = [0, 0, 0, 0, 0, 0, 0, 0, 0,]

        if not ctx['num'] == 0:
            for note in notes:
                if note.lp_team == True:
                    ctx['h_lp'] += 1
                else:
                    ctx['a_lp'] += 1

                if note.nlp_team == True:
                    ctx['h_nlp'] += 1
                else:
                    ctx['a_nlp'] += 1

                if note.b_or_s == True:
                    ctx['b'] += 1
                else:
                    ctx['s'] += 1

                if note.choice_team == True:
                    ctx['h_wdp'][note.wpd_num - 1] += 1
                else:
                    ctx['a_wdp'][note.wpd_num - 1] += 1

            ctx['h_lp_p'] = float(ctx['h_lp']) / ctx['num'] * 100
            ctx['a_lp_p'] = float(ctx['a_lp']) / ctx['num'] * 100

            ctx['h_nlp_p'] = float(ctx['h_nlp']) / ctx['num'] * 100
            ctx['a_nlp_p'] = float(ctx['a_nlp']) / ctx['num'] * 100

            ctx['b_p'] = float(ctx['b']) / ctx['num'] * 100
            ctx['s_p'] = float(ctx['s']) / ctx['num'] * 100

            ctx['h_wdp_p'] = [float(wdp) / ctx['num'] * 100 for wdp in ctx['h_wdp']]
            ctx['a_wdp_p'] = [float(wdp) / ctx['num'] * 100 for wdp in ctx['a_wdp']]





        
        return ctx

        



