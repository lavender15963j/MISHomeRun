#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""NBaseball URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from main import views as mainView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Iuno.member
    url(r'^accounts/', include("Iuno.member.urls")),

    # main
    url(r'', include("main.urls", namespace='main')),

    # customer
    url(r'^customer/', include("customer.urls", namespace='customer')),

    # betting
    url(r'^betting/', include("betting.urls", namespace='betting')),

    # team
    url(r'^team/', include("team.urls", namespace='team')),

    # forum
    url(r'^forum/', include("forum.urls", namespace='forum')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

