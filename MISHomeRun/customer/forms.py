#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from customer.models import RealNote

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

    wpd1 = forms.IntegerField(label='wpd1', min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'value': 0,}))

    wpd2 = forms.IntegerField(label='wpd2', min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'value': 0,}))
    
    wpd3 = forms.IntegerField(label='wpd3', min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'value': 0,}))
    
    wpd4 = forms.IntegerField(label='wpd4', min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'value': 0,}))

    wpd5 = forms.IntegerField(label='wpd5', min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'value': 0,}))
    
    wpd6 = forms.IntegerField(label='wpd6', min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'value': 0,}))                                    
    
    wpd7 = forms.IntegerField(label='wpd7', min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'value': 0,}))

    wpd8 = forms.IntegerField(label='wpd8', min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'value': 0,}))
    
    wpd9 = forms.IntegerField(label='wpd9', min_value=0,
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
            'wpd1',
            'wpd2',
            'wpd3',
            'wpd4',
            'wpd5',
            'wpd6',
            'wpd7',
            'wpd8',
            'wpd9',
        ]