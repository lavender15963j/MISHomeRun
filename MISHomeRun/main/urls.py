#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.HomwView.as_view(), name='home'),
]