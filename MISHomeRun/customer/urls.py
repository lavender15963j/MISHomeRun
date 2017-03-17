#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

app_name = 'customer'

urlpatterns = [
    url(r'^(?P<username>\w+)/$', views.ProfileView.as_view(), name='profile'),
    url(r'^(?P<username>\w+)/realnote/$', views.RealNoteView.as_view(), name='real'),
    url(r'^(?P<username>\w+)/fakenote/$', views.FakeNoteView.as_view(), name='fake'),
    url(r'^buyfakenote$', views.PurchaseView.as_view(), name='purchase'),
]