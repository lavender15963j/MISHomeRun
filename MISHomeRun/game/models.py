#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone

class Game(models.Model):
    game_no = models.IntegerField()
    stadium = models.CharField(max_length=10)
    date = models.DateTimeField()

    away_team = models.ForeignKey(
        'team.Team',
        on_delete=models.CASCADE,
        related_name='away_team',
    )
    home_team = models.ForeignKey(
        'team.Team',
        on_delete=models.CASCADE,
        related_name='home_team',
    )

    # data
    winner = models.NullBooleanField()

    away_team_score = models.IntegerField(blank=True, null=True)
    home_team_score = models.IntegerField(blank=True, null=True)

    @property
    def is_final(self):
        if self.winner is None:
            nowtime = timezone.now()
            if self.date < nowtime:
                return True
            return False
        else:
            return True


    def __unicode__(self):
        return u"%d: %s v.s. %s" % (self.game_no, self.home_team, self.away_team)
