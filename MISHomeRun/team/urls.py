#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views
from views import Teammain,Teamdetail

app_name = 'team'

urlpatterns = [
    url(r'^$', Teammain, name = 'team1'),
    url(r'^(\w+)$', Teamdetail, name = 'teamspecific'),
]