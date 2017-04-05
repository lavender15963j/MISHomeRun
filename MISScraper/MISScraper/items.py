# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy_djangoitem import DjangoItem
from game.models import Game
from team.models import Team

class GameItem(scrapy.Item):
    django_model = Game
    
class TeamItem(scrapy.Item):
    django_model = Team

