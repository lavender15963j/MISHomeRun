#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views
from views import *

app_name = 'team'

urlpatterns = [
    url(r'^introduction/$', Teammain, name = 'team1'),
    url(r'^introduction/(\w+)$', Teamdetail, name = 'teamspecific'),
    url(r'^stat/$', Statmain, name = 'stat1'),
    url(r'^stat/(\w+)$', Statdetail, name = 'statspecfic'),
]