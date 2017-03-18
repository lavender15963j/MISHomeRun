#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

class FakeNoteForm(forms.Form):
    betting = forms.CharField(max_length=1)
    lp = forms.CharField(max_length=1)
    nlp = forms.CharField(max_length=1)
    bs = forms.CharField(max_length=1)
    choice = forms.CharField(max_length=1)
    wpd = forms.CharField(max_length=1)