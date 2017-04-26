#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
import pytz
import datetime

from django.utils.dateparse import parse_datetime
from django.db import transaction
from Iuppiter.Encoding import _unicode

from team.models import Team 
from game.models import Game
from betting.models import Betting

class BettingSpider(scrapy.Spider):
    name = "bettingspider"
    
    def start_requests(self):
        attr = ['today', 'tomorrow',]
        for a in attr:
            url = 'https://www.playsport.cc/predictgame.php?allianceid=6&gameday=%s' % a
            print '-----Start download %s -----' % url
            yield scrapy.Request(url=url, callback=self.parse)
            
    def getTeam(self, teamName):
        teamName = teamName.strip()
        if teamName == u"\u4e2d\u4fe1\u5144\u5f1f": # 中信兄弟
            code = "E02"
        elif teamName == u"\u7d71\u4e00\u7345": # 統一獅
            code = "L01"
        elif teamName == u"Lamigo\u6843\u733f": # Lamigo桃猿
            code = "A02"
        elif teamName == u"\u7fa9\u5927": #富邦
            code = "B04"
        else:
            return None
        team = Team.objects.get(code=code)
        return team
            
    def parse(self, response):
    
        game_no = response.css('.predictgame-table tr[gameid] td.td-gameinfo h3::text').extract()
        time = response.css('.predictgame-table tr[gameid] td.td-gameinfo h4::text').extract()
        
        team = response.css('.predictgame-table tr[gameid] td.td-teaminfo a::text').extract()
        h_or_a = response.css('.predictgame-table tr[gameid] td.td-bank-bet01 label>strong::text').extract()
        h_or_a = [h_or_a[i] for i in range(0, len(h_or_a ), 2)]
        
        # lp
        lp_num = response.css('.predictgame-table tr[gameid] td.td-bank-bet01 label>span>strong::text').extract()
        PN = [num[i][0] for num in lp_num]
        lp_num = [float(lp_num[i][1:]) for i in range(0, len(lp_num), 2)]
       
        lp_odd = response.css('.predictgame-table tr[gameid] td.td-bank-bet01 label>span>span::text').extract()
        lp_odd = [float(odd[2:]) for odd in lp_odd]
        
        # nlp
        nlp_odd = response.css('.predictgame-table tr[gameid] td.td-bank-bet03 label>span>span::text').extract()
        nlp_odd = [float(odd) for odd in nlp_odd]
        
        # bs 
        bs_num = response.css('.predictgame-table tr[gameid] td.td-bank-bet02 label>span>strong::text').extract()
        bs_odd = response.css('.predictgame-table tr[gameid] td.td-bank-bet02 label>span>span::text').extract()
        
        bs_num = [bs_num[i] for i in range(0, len(bs_num), 2)]
        bs_odd = [float(odd[2:]) for odd in bs_odd]
        
        # time
        today = response.url[response.url.index('gameday=') + 8:]
        
        td = datetime.datetime.today()
        if today == 'yesterday':
            td = td - datetime.timedelta(days=1)
        elif today == 'tomorrow':
            td = td + datetime.timedelta(days=1)
        else:
            td = datetime.datetime.today()
        td = td.strftime("%Y-%m-%d")
        
        # game and betting
        for i, g in enumerate(game_no, 0):
            f_i = i * 2
            s_i = f_i + 1
        
            if 'AM' in time[i]:
                t = time[i][4:]
            else:
                t = time[i][4:].split(":")
                t[0] = str(int(t[0]) + 12)
                t = ":".join(t)
             
            naive = parse_datetime("%s %s:00" % (td, t))
            dt = pytz.timezone("Asia/Taipei").localize(naive, is_dst=None) + datetime.timedelta(minutes=5)
            
            if h_or_a[i] == u'\u5ba2': #客
                at = self.getTeam(team[f_i])
                ht = self.getTeam(team[s_i])
                h_PN = PN[s_i]
                h_lp = lp_odd[s_i]
                a_lp = lp_odd[f_i]
                h_nlp = nlp_odd[s_i]
                a_nlp = nlp_odd[f_i]
                
            else:
                at = self.getTeam(team[s_i])
                ht = self.getTeam(team[f_i])
                h_PN = PN[f_i]
                h_lp = lp_odd[f_i]
                a_lp = lp_odd[s_i]
                h_nlp = nlp_odd[f_i]
                a_nlp = nlp_odd[s_i]
                
            if h_PN == u'+':
                h_PN = True
            else:
                h_PN = False
                
            game, created = Game.objects.get_or_create(
                date=dt,
                away_team=at,
                home_team=ht,
                defaults={
                    'game_no': int(g),
                    'stadium': '-',
                },
            )
            
            betting, created = Betting.objects.get_or_create(
                game=game,
                defaults={
                    'home_team_PN': h_PN,
                    
                    'let_point_number': lp_num[i],
                    'lp_home_team_odds': h_lp,
                    'lp_away_team_odds': a_lp,
                    
                    'nlp_home_team_odds': h_nlp,
                    "nlp_away_team_odds": a_nlp,
                    
                    "big_small_point_number": bs_num[i],
                    "big_odds": bs_odd[f_i],
                    "small_odds": bs_odd[s_i],
                    
                    "h_odds1": 0.0,
                    "h_odds2": 0.0,
                    "h_odds3": 0.0,
                    "h_odds4": 0.0,
                    "h_odds5": 0.0,
                    "h_odds6": 0.0,
                    "h_odds7": 0.0,
                    "h_odds8": 0.0,
                    "h_odds9": 0.0,
                    
                    "a_odds1": 0.0,
                    "a_odds2": 0.0,
                    "a_odds3": 0.0,
                    "a_odds4": 0.0,
                    "a_odds5": 0.0,
                    "a_odds6": 0.0,
                    "a_odds7": 0.0,
                    "a_odds8": 0.0,
                    "a_odds9": 0.0,
                },
            )
            
        