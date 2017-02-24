#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Betting(models.Model):
    game = models.OneToOneField(
        'game.Game',
        on_delete=models.CASCADE,
    )

    POSITIVE_NEGATIVE_CHOICES = (
        ('+', '+'),
        ('-', '-'),
    )

    home_team_PN = models.CharField(max_length=5, 
                                   choices=POSITIVE_NEGATIVE_CHOICES)

    def __unicode__(self):
        return u"Betting For No.%d" % self.game.game_no

class LetPoint(models.Model):
    let_point_number = models.DecimalField(max_digits=4, decimal_places=2)
    home_team_odds = models.DecimalField(max_digits=4, decimal_places=2)
    away_team_odds = models.DecimalField(max_digits=4, decimal_places=2)

    betting = models.OneToOneField(
        'betting.Betting',
        on_delete=models.CASCADE,
    )

    def __unicode__(self):
        return u"LetPoint For No.%d" % self.betting.game.game_no

class NoLetPoint(models.Model):
    home_team_odds = models.DecimalField(max_digits=4, decimal_places=2)
    away_team_odds = models.DecimalField(max_digits=4, decimal_places=2)

    betting = models.OneToOneField(
        'betting.Betting',
        on_delete=models.CASCADE,
    )

    def __unicode__(self):
        return u"NoLetPoint For No.%d" % self.betting.game.game_no

class BigSmallPoint(models.Model):
    big_small_point_number = models.DecimalField(max_digits=4, decimal_places=2)
    big_odds = models.DecimalField(max_digits=4, decimal_places=2)
    small_odds = models.DecimalField(max_digits=4, decimal_places=2)

    betting = models.OneToOneField(
        'betting.Betting',
        on_delete=models.CASCADE,
    )

    def __unicode__(self):
        return u"BigSmallPoint For No.%d" % self.betting.game.game_no

class WinPointDiff(models.Model):
    odds1 = models.DecimalField(max_digits=4, decimal_places=2)
    odds2 = models.DecimalField(max_digits=4, decimal_places=2)
    odds3 = models.DecimalField(max_digits=4, decimal_places=2)
    odds4 = models.DecimalField(max_digits=4, decimal_places=2)
    odds5 = models.DecimalField(max_digits=4, decimal_places=2)
    odds6 = models.DecimalField(max_digits=4, decimal_places=2)
    odds7 = models.DecimalField(max_digits=4, decimal_places=2)
    odds8 = models.DecimalField(max_digits=4, decimal_places=2)
    odds9 = models.DecimalField(max_digits=4, decimal_places=2)

    betting = models.OneToOneField(
        'betting.Betting',
        on_delete=models.CASCADE,
    )

    def __unicode__(self):
        return u"WinPointDiff For No.%d" % self.betting.game.game_no