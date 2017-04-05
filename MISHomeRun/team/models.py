#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Team(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True,
        height_field = "height_field",
        width_field = "width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    URL = models.URLField(max_length=200, null=True)
    Coach = models.CharField(max_length=20, null=True)
    date = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.name

    @property
    def get_teamdata(self):
        return Stat.objects.filter(name = self)

class Stat(models.Model):
    #Team name
    name = models.ForeignKey(
        'Team',
        on_delete=models.CASCADE,
    )

    #Code
    code = models.CharField(default=0, max_length=10)

    #year
    year = models.IntegerField(max_length=10)
    
    #團隊成績
    Team_1_G = models.IntegerField(default = 0,null=True, blank=True)
    Team_1_W = models.IntegerField(default = 0,null=True, blank=True)
    Team_1_L = models.IntegerField(default = 0,null=True, blank=True)
    Team_1_T = models.IntegerField(default = 0,null=True, blank=True)
    Team_1_PCT = models.FloatField(default = 0,null=True, blank=True)
    Team_1_Whome = models.IntegerField(default = 0,null=True, blank=True)
    Team_1_Lhome = models.IntegerField(default = 0,null=True, blank=True)
    Team_1_Thome = models.IntegerField(default = 0,null=True, blank=True)
    Team_1_Waway = models.IntegerField(default = 0,null=True, blank=True)
    Team_1_Laway = models.IntegerField(default = 0,null=True, blank=True)
    Team_1_Taway = models.IntegerField(default = 0,null=True, blank=True)
    Team_2_G = models.IntegerField(default = 0,null=True, blank=True)
    Team_2_W = models.IntegerField(default = 0,null=True, blank=True)
    Team_2_L = models.IntegerField(default = 0,null=True, blank=True)
    Team_2_T = models.IntegerField(default = 0,null=True, blank=True)
    Team_2_PCT = models.FloatField(default = 0,null=True, blank=True)
    Team_2_Whome = models.IntegerField(default = 0,null=True, blank=True)
    Team_2_Lhome = models.IntegerField(default = 0,null=True, blank=True)
    Team_2_Thome = models.IntegerField(default = 0,null=True, blank=True)
    Team_2_Waway = models.IntegerField(default = 0,null=True, blank=True)
    Team_2_Laway = models.IntegerField(default = 0,null=True, blank=True)
    Team_2_Taway = models.IntegerField(default = 0,null=True, blank=True)


    #投手成績
    Pitch_ERA = models.FloatField(default = 0,null=True, blank=True)
    Pitch_IP = models.FloatField(default = 0,null=True, blank=True)
    Pitch_BF = models.IntegerField(default = 0,null=True, blank=True)
    Pitch_H = models.IntegerField(default = 0,null=True, blank=True)
    Pitch_HR = models.IntegerField(default = 0,null=True, blank=True)
    Pitch_SO = models.IntegerField(default = 0,null=True, blank=True)
    Pitch_WP = models.IntegerField(default = 0,null=True, blank=True)
    Pitch_BK = models.IntegerField(default = 0,null=True, blank=True)
    Pitch_R = models.IntegerField(default = 0,null=True, blank=True)
    Pitch_ER = models.IntegerField(default = 0,null=True, blank=True)

    #打擊成績
    Hit_AVG = models.FloatField(default = 0,null=True, blank=True)
    Hit_G = models.IntegerField(default = 0,null=True, blank=True)
    Hit_AB = models.IntegerField(default = 0,null=True, blank=True)
    Hit_R = models.IntegerField(default = 0,null=True, blank=True)
    Hit_RBI = models.IntegerField(default = 0,null=True, blank=True)
    Hit_H = models.IntegerField(default = 0,null=True, blank=True)
    Hit_HR = models.IntegerField(default = 0,null=True, blank=True)
    Hit_SAC = models.IntegerField(default = 0,null=True, blank=True)
    Hit_SO = models.IntegerField(default = 0,null=True, blank=True)
    Hit_SB = models.IntegerField(default = 0,null=True, blank=True)
    Hit_OBP = models.FloatField(default = 0,null=True, blank=True)
    Hit_SLG = models.FloatField(default = 0,null=True, blank=True)

    #守備成績
    Defense_FPCT = models.FloatField(default = 0,null=True, blank=True)
    Defense_TC = models.IntegerField(default = 0,null=True, blank=True)
    Defense_PO = models.IntegerField(default = 0,null=True, blank=True)
    Defense_A = models.IntegerField(default = 0,null=True, blank=True)
    Defense_DP = models.IntegerField(default = 0,null=True, blank=True)
    Defense_E = models.IntegerField(default = 0,null=True, blank=True)
    Defense_CS = models.IntegerField(default = 0,null=True, blank=True)
    Defense_PB = models.IntegerField(default = 0,null=True, blank=True)
    

    # def PCT1(self):
    #     return self.Team_1_W/self.Team_1_G
    
    # def PCT2(self):
    #     return self.Team_2_W/self.Team_2_G

    def __unicode__(self):
        return u"%s-%d" % (self.name, self.year)

