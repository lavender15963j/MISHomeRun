#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

app_name = 'betting'

urlpatterns = [
    url(r'^prediction/$', views.PredictionView.as_view(), name='prediction'),
    url(r'^prediction/(?P<pk>\d+)/$', views.BettingDetailView.as_view(), name='detail'),
    url(r'^statistics/$', views.StatisticsView.as_view(), name='statistics'),
]