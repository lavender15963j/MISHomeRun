#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy

from MISScraper.items import GameItem

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

    def parse(self, response):
        games = GameItem.django_model.objects.all()
        print games
        pass
