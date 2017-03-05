#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

app_name = 'betting'

urlpatterns = [
    url(r'^prediction/$', views.PredictionView.as_view(), name='prediction'),
]