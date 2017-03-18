#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    coin = models.IntegerField(default=4)
    level = models.IntegerField(default=1)
    team = models.ForeignKey(
        'team.Team',
        on_delete=models.CASCADE,
        related_name='favor',
        null=True,
    )

    #勝率 wp=Winning percentage
    lp_wp = models.IntegerField(null=True, blank=True)
    nlp_wp = models.IntegerField(null=True, blank=True)
    bs_wp = models.IntegerField(null=True, blank=True)
    wdp_wp = models.IntegerField(null=True, blank=True)
    all_wp = models.IntegerField(null=True, blank=True)

