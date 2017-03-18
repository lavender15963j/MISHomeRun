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
    h_odds1 = models.DecimalField(max_digits=4, decimal_places=2)
    h_odds2 = models.DecimalField(max_digits=4, decimal_places=2)
    h_odds3 = models.DecimalField(max_digits=4, decimal_places=2)
    h_odds4 = models.DecimalField(max_digits=4, decimal_places=2)
    h_odds5 = models.DecimalField(max_digits=4, decimal_places=2)
    h_odds6 = models.DecimalField(max_digits=4, decimal_places=2)
    h_odds7 = models.DecimalField(max_digits=4, decimal_places=2)
    h_odds8 = models.DecimalField(max_digits=4, decimal_places=2)
    h_odds9 = models.DecimalField(max_digits=4, decimal_places=2)

    a_odds1 = models.DecimalField(max_digits=4, decimal_places=2)
    a_odds2 = models.DecimalField(max_digits=4, decimal_places=2)
    a_odds3 = models.DecimalField(max_digits=4, decimal_places=2)
    a_odds4 = models.DecimalField(max_digits=4, decimal_places=2)
    a_odds5 = models.DecimalField(max_digits=4, decimal_places=2)
    a_odds6 = models.DecimalField(max_digits=4, decimal_places=2)
    a_odds7 = models.DecimalField(max_digits=4, decimal_places=2)
    a_odds8 = models.DecimalField(max_digits=4, decimal_places=2)
    a_odds9 = models.DecimalField(max_digits=4, decimal_places=2)

    def __unicode__(self):
        return u"Betting For No.%d" % self.game.game_no