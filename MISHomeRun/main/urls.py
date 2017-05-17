#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.HomwView.as_view(), name='home'),
    url(r'^tbetting1/$', views.T1View.as_view(), name='t1'),
    url(r'^tbetting2/$', views.T2View.as_view(), name='t2'),
]