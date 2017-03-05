#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Betting(models.Model):
    game = models.OneToOneField(
        'game.Game',
        on_delete=models.CASCADE,
    )

    home_team_PN = models.BooleanField()

    # Let Point
    let_point_number = models.DecimalField(max_digits=4, decimal_places=2)
    lp_home_team_odds = models.DecimalField(max_digits=4, decimal_places=2)
    lp_away_team_odds = models.DecimalField(max_digits=4, decimal_places=2)

    # No Let Point
    nlp_home_team_odds = models.DecimalField(max_digits=4, decimal_places=2)
    nlp_away_team_odds = models.DecimalField(max_digits=4, decimal_places=2)

    # No Let Point
    big_small_point_number = models.DecimalField(max_digits=4, decimal_places=2)
    big_odds = models.DecimalField(max_digits=4, decimal_places=2)
    small_odds = models.DecimalField(max_digits=4, decimal_places=2)

    # Win Point Diff
    odds1 = models.DecimalField(max_digits=4, decimal_places=2)
    odds2 = models.DecimalField(max_digits=4, decimal_places=2)
    odds3 = models.DecimalField(max_digits=4, decimal_places=2)
    odds4 = models.DecimalField(max_digits=4, decimal_places=2)
    odds5 = models.DecimalField(max_digits=4, decimal_places=2)
    odds6 = models.DecimalField(max_digits=4, decimal_places=2)
    odds7 = models.DecimalField(max_digits=4, decimal_places=2)
    odds8 = models.DecimalField(max_digits=4, decimal_places=2)
    odds9 = models.DecimalField(max_digits=4, decimal_places=2)

    def __unicode__(self):
        return u"Betting For No.%d" % self.game.game_no