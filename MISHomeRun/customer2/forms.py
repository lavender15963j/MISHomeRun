#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from customer2.models import RealNote

class PurchaseForm(forms.Form):
    buy_for = forms.CharField(max_length=5)
    buy_note = forms.CharField(max_length=10)
    cost = forms.CharField(max_length=5)


class RealNoteForm(forms.ModelForm):
    lp_home_team = forms.IntegerField(label='lp_home_team', min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'value': 0,}))

    lp_away_team = forms.IntegerField(label='lp_away_team', min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'value': 0,}))

    nlp_home_team = forms.IntegerField(label='nlp_home_team', min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'value': 0,}))
    
    nlp_away_team = forms.IntegerField(label='nlp_away_team', min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'value': 0,}))
    
    big = forms.IntegerField(label='big', min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'value': 0,}))

    small = forms.IntegerField(label='small', min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'value': 0,}))

    class Meta:
        model = RealNote
        fields = [
            'betting', 
            'lp_home_team', 
            'lp_away_team', 
            'nlp_home_team', 
            'nlp_away_team',
            'big',
            'small',
        ]