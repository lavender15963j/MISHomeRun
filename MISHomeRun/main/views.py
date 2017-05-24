#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views import generic

from main.mixins import PageTitleMixin
from machina.core.db.models import get_model
from django.db.models import Q

from main.models import User
from team.models import Team
from game.models import Game
from customer2.models import FakeNote
from betting.models import Betting

Topic = get_model('forum_conversation', 'Topic')


class HomwView(PageTitleMixin, generic.TemplateView):
    template_name = 'indexContent.html'
    page_title = '首頁'
    active_tab = 'home'

    def get_context_data(self, **kwargs):
        ctx = super(HomwView, self).get_context_data(**kwargs)

        # 熱門文章
        topics = Topic.objects.all().order_by('-posts_count')
        if len(topics) > 10:
            ctx['topics'] = topics[:10]
        else:
            ctx['topics'] = topics

        # 投注排行榜
        lp_users = User.objects.exclude(lp_wp=None).order_by('-lp_wp')
        if len(lp_users) > 3:
            ctx['lp_users'] = lp_users[:3]
        else:
            ctx['lp_users'] = lp_users

        nlp_users = User.objects.exclude(nlp_wp=None).order_by('-nlp_wp')
        if len(nlp_users) > 3:
            ctx['nlp_users'] = nlp_users[:3]
        else:
            ctx['nlp_users'] = nlp_users

        bs_users = User.objects.exclude(bs_wp=None).order_by('-bs_wp')
        if len(bs_users) > 3:
            ctx['bs_users'] = bs_users[:3]
        else:
            ctx['bs_users'] = bs_users

        wdp_users = User.objects.exclude(wdp_wp=None).order_by('-wdp_wp')
        if len(wdp_users) > 3:
            ctx['wdp_users'] = wdp_users[:3]
        else:
            ctx['wdp_users'] = wdp_users

        all_users = User.objects.exclude(all_wp=None).order_by('-all_wp')
        if len(all_users) > 3:
            ctx['all_users'] = all_users[:3]
        else:
            ctx['all_users'] = all_users

        # 本季戰績
        class TeamData(object):
            def __init__(self, t):
                self.team = t
                self.games = Game.objects.filter(Q(away_team=t, date__year=2017)|Q(home_team=t, date__year=2017))

            @property
            def wt(self):
                time = 0
                for g in self.games:
                    if g.winner == True:
                        winner = g.home_team
                    elif g.winner == False:
                        winner = g.away_team
                    else:
                        winner = None
                    
                    if winner == self.team:
                        time += 1
                return time

            @property
            def lt(self):
                time = 0
                for g in self.games:
                    if g.winner == True:
                        winner = g.home_team
                    elif g.winner == False:
                        winner = g.away_team
                    else:
                        winner = None
                    
                    if not winner == self.team and not winner == None:
                        time += 1
                return time

            @property
            def dt(self):
                time = 0
                for g in self.games:
                    if g.winner == None and g.away_team_score is not None and g.home_team_score is not None:
                        time += 1
                return time

            @property
            def wp(self):
                return "%.1f" % (float(self.wt) / self.games.count() * 100)

        teams = []
        for t in Team.objects.all():
            td = TeamData(t)
            teams.append(td)

        ctx['teams'] = teams

        # 投注賽事
        bettings = Betting.objects.all().order_by('-game__date')
        if len(bettings) > 5:
            ctx['bettings'] = bettings[:5]
        else:
            ctx['bettings'] = bettings

        # 投注情形
        for b in bettings:
            if b.game.is_final:
                betting = b
                break
        ctx['game'] = betting.game
        notes = FakeNote.objects.filter(betting=betting)
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

class T1View(PageTitleMixin, generic.TemplateView):
    template_name = 'main/t_betting1.html'
    page_title = '玩法介紹'

class T2View(PageTitleMixin, generic.TemplateView):
    template_name = 'main/t_play.html'
    page_title = '投注單介紹'

class T3View(PageTitleMixin, generic.TemplateView):
    template_name = 'main/t_coin.html'
    page_title = '金幣與階級介紹'
    

