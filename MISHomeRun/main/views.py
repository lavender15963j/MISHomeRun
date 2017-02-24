#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views import generic

from main.mixins import PageTitleMixin

class HomwView(PageTitleMixin, generic.TemplateView):
    template_name = 'index.html'
    page_title = '首頁'
    active_tab = 'home'

    def get_context_data(self, **kwargs):
        ctx = super(HomwView, self).get_context_data(**kwargs)
        return ctx
