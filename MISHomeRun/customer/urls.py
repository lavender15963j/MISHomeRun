#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

app_name = 'customer'

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.ProfileView.as_view(), name='profile'),
    url(r'^(?P<pk>\d+)/realnote/$', views.RealNoteView.as_view(), name='real'),
    url(r'^(?P<pk>\d+)/fakenote/$', views.FakeNoteView.as_view(), name='fake'),
]