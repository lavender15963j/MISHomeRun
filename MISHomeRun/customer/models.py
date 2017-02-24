#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Note(models.Model):
    TYPE_CHOICES = (
        ('fake', 'Fake'),
        ('real', 'Real'),
    )

    note_type = models.CharField(max_length=5, 
                                 choices=TYPE_CHOICES)

    betting = models.ForeignKey(
        'betting.Betting',
        on_delete=models.CASCADE,
        related_name='betting',
    )

    user = models.ForeignKey(
        'main.User',
        on_delete=models.CASCADE,
        related_name='user',
    )

    # Let Point
    lp_home_team = models.IntegerField(default=0)
    lp_away_team = models.IntegerField(default=0)

    # No Let Point
    nlp_home_team = models.IntegerField(default=0)
    nlp_away_team = models.IntegerField(default=0)

    # Big Small Point
    big = models.IntegerField(default=0)
    small = models.IntegerField(default=0)

    # Win Point Diff
    wpd1 = models.IntegerField(default=0)
    wpd2 = models.IntegerField(default=0)
    wpd3 = models.IntegerField(default=0)
    wpd4 = models.IntegerField(default=0)
    wpd5 = models.IntegerField(default=0)
    wpd6 = models.IntegerField(default=0)
    wpd7 = models.IntegerField(default=0)
    wpd8 = models.IntegerField(default=0)
    wpd9 = models.IntegerField(default=0)

    def __unicode__(self):
        return u"%s's %s Note For No.%d" % (self.user.username, self.note_type, 
                                            self.betting.game.game_no)

