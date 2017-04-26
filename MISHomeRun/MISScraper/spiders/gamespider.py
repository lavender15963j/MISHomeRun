#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
import pytz

from django.utils.dateparse import parse_datetime
from django.db import transaction
from Iuppiter.Encoding import _unicode

from MISScraper.items import GameItem
from team.models import Team 
from game.models import Game


class GamespiderSpider(scrapy.Spider):
    name = "gamespider"
    
    def start_requests(self):
        # http://www.cpbl.com.tw/web/team_dayscore.php?&gameno=01&team=E02&stype=&sbteamno=&syear=2017
        years = ['2017', '2016', '2015', '2014',]
        urls = []
        teams = ['E02', 'L01', 'A02', 'B04',]
        for team in teams:
            for year in years:
                url = 'http://www.cpbl.com.tw/web/team_dayscore.php?&gameno=01&team=%s&stype=&sbteamno=&syear=%s' % (team, year)
                urls.append(url)
        
        for url in urls:
            print '-----Start download %s -----' % url
            yield scrapy.Request(url=url, callback=self.parse)
            
    def getTeam(self, teamName):
        teamName = teamName.strip()
        if teamName == u"\u4e2d\u4fe1\u5144\u5f1f": # 中信兄弟
            code = "E02"
        elif teamName == u"\u7d71\u4e007-ELEVEn": # 統一7-ELEVEn獅
            code = "L01"
        elif teamName == u"Lamigo": # Lamigo桃猿
            code = "A02"
        elif teamName == u"\u5bcc\u90a6": #富邦
            code = "B04"
        else:
            return None
        team = Team.objects.get(code=code)
        return team

    @transaction.atomic
    def parse(self, response):
        teams = Team.objects.all()
        
        game_no = response.css('table.mix_x tr td:nth-child(1)::text').extract()
        stadium = response.css('table.mix_x tr td:nth-child(2)::text').extract()
        date = response.css('table.mix_x tr td:nth-child(3)::text').extract()
        time = response.css('table.mix_x tr td:nth-child(4)::text').extract()
        away_team = response.css('table.mix_x tr td:nth-child(5) a::text').extract()
        away_team_score = response.css('table.mix_x tr td:nth-child(6)::text').extract()
        home_team = response.css('table.mix_x tr td:nth-child(7) a::text').extract()
        home_team_score = response.css('table.mix_x tr td:nth-child(8)::text').extract()
        win_team = response.css('table.mix_x tr td:nth-child(9)::text').extract()
        
        for i, g in enumerate(game_no, 0):
            naive = parse_datetime("%s %s:00" % (date[i], time[i]))
            dt = pytz.timezone("Asia/Taipei").localize(naive, is_dst=None)
            
            at = self.getTeam(away_team[i])
            ht = self.getTeam(home_team[i])
            
            if not at or not ht:
                continue

            wt = self.getTeam(win_team[i])
            
            winner = None
            if ht == wt:
                winner = True
            elif at == wt:
                winner = False
            else:
                winner = None

            obj, created = Game.objects.update_or_create(
                date=dt,
                away_team=at,
                home_team=ht,
                defaults={
                    'game_no': int(g),
                    'stadium': stadium[i],
                    'winner': winner,
                    'away_team_score': int(away_team_score[i]),
                    'home_team_score': int(home_team_score[i]),
                },
            )
            
            
           
       
        
        
