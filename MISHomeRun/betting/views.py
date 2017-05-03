#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytz
import datetime

from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.dateparse import parse_datetime
from django.db.models import Q

from betting.models import Betting
from team.models import Team
from game.models import Game
from customer.models import FakeNote
from main.mixins import PageTitleMixin
from betting.forms import FakeNoteForm

class StatisticsView(PageTitleMixin, generic.TemplateView):
    template_name = 'betting/statistics.html'
    page_title = '數據分析'

    def get_context_data(self, **kwargs):
        ctx = super(StatisticsView, self).get_context_data(**kwargs)

        ctx['t'] = int(self.request.GET.get('t', 150))
        wt = self.request.GET.get('win', None)
        lt = self.request.GET.get('lose', None)
        if not lt == "0" and not wt == "0":
            if lt and wt:
                ctx['win_t'] = Team.objects.get(code=wt)
                ctx['lose_t'] = Team.objects.get(code=lt)

                ctx['wtc'] = wt
                ctx['ltc'] = lt
            else:
                ctx['win_t'] = Team.objects.get(code='E02')
                ctx['lose_t'] = Team.objects.get(code='A02')

                ctx['wtc'] = '0'
                ctx['ltc'] = '0'
        else:
            ctx['win_t'] = Team.objects.get(code='E02')
            ctx['lose_t'] = Team.objects.get(code='A02')

            ctx['wtc'] = '0'
            ctx['ltc'] = '0'

        games = Game.objects.filter(Q(away_team=ctx['win_t'], home_team=ctx['lose_t'])|Q(home_team=ctx['win_t'], away_team=ctx['lose_t'])).order_by('-date')
        t_num = Game.objects.filter(Q(away_team=ctx['win_t'], home_team=ctx['lose_t'])|Q(home_team=ctx['win_t'], away_team=ctx['lose_t'])).count()
       
        if t_num > ctx['t']:
            games = games[:ctx['t']]
        else:
            ctx['t'] = t_num
        
        # G1
        lp_p = []
        lp_wt = []
        lp_lt = []
        for g in games:
            if g.winner == True:
                winner = g.home_team
                lp = g.home_team_score - g.away_team_score
            elif g.winner == False:
                winner = g.away_team
                lp = g.away_team_score - g.home_team_score
            else:
                continue
            lp = abs(lp)
            if len(lp_p) < lp:
                lp_p = [i for i in range(1, lp + 1)]
                for i in range(0, len(lp_p) - len(lp_wt)):
                    lp_wt.append(0)
                    lp_lt.append(0)

            if ctx['win_t'] == winner:
                lp_wt[lp - 1] += 1
            else:
                lp_lt[lp - 1] += 1

        ctx['lp_p'] = lp_p
        ctx['lp_wt'] = lp_wt
        ctx['lp_lt'] = lp_lt

        # G2
        tp_dir = {}
        for g in games:
            total = g.away_team_score + g.home_team_score
            if str(total) in tp_dir:
                tp_dir[str(total)] += 1
            else:
                tp_dir[str(total)] = 1

        tp_p = []
        tp = []

        key = []
        for k in tp_dir:
            key.append(int(k))
        
        for k in sorted(key):
            tp_p.append(int(k))
            tp.append(tp_dir[str(k)])
        ctx['tp_p'] = tp_p
        ctx['tp'] = tp

        # G3
        w_t = [0, 0]
        for g in games:
            if g.winner == True:
                winner = g.home_team
            elif g.winner == False:
                winner = g.away_team
            else:
                continue

            if ctx['win_t'] == winner:
                w_t[0] += 1
            else:
                w_t[1] += 1
        ctx['w_t'] = w_t

        # G4
        wpd = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for g in games:
            if g.winner == True:
                winner = g.home_team
                lp = g.home_team_score - g.away_team_score
            elif g.winner == False:
                winner = g.away_team
                lp = g.away_team_score - g.home_team_score
            else:
                continue
            lp = abs(lp)

            if winner == ctx['win_t']:
                if lp >= 9:
                    wpd[8] += 1
                else:
                    wpd[lp - 1] += 1
        ctx['wpd'] = wpd
        
        return ctx

class PredictionView(PageTitleMixin, FormView):
    template_name = 'betting/prediction.html'
    page_title = '投注資訊'
    form_class = FakeNoteForm
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PredictionView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(PredictionView, self).get_context_data(**kwargs)

        td = datetime.datetime.today()
        td = td + datetime.timedelta(days=1)
        td = td.strftime("%Y-%m-%d")
        ctx['bettings'] = Betting.objects.filter(game__date__lt=td).order_by('-game__date')
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

        



