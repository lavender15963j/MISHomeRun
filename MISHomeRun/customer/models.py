#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class RealNote(models.Model):
    betting = models.ForeignKey(
        'betting.Betting',
        on_delete=models.CASCADE,
        related_name='betting_real',
    )

    user = models.ForeignKey(
        'main.User',
        on_delete=models.CASCADE,
        related_name='user_real',
    )
    
    create_date = models.DateTimeField()

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
                                            
class FakeNote(models.Model):
    betting = models.ForeignKey(
        'betting.Betting',
        on_delete=models.CASCADE,
        related_name='betting_fake',
    )

    user = models.ForeignKey(
        'main.User',
        on_delete=models.CASCADE,
        related_name='user_fake',
    )

    create_date = models.DateTimeField()

    # Let Point
    lp_team = models.BooleanField()

    # No Let Point
    nlp_team = models.BooleanField()

    # No Let Point
    b_or_s = models.BooleanField()

    # Win Point Diff
    wpd1 = models.IntegerField()

class SystemGiveRecord(models.Model):
    receiver = models.ForeignKey(
        'main.User',
        on_delete=models.CASCADE,
        related_name='receiver',
    )

    create_date = models.DateTimeField()

    give_coins = models.IntegerField()

    reason = models.TextField(blank=True)

class PurchaseRecord(models.Model):
    buyer = models.ForeignKey(
        'main.User',
        on_delete=models.CASCADE,
        related_name='buyer',
    )

    buy_note = models.ForeignKey(
        'customer.FakeNote',
        on_delete=models.CASCADE,
        related_name='buy_note',
    )

    b_lp = models.BooleanField()
    b_nlp = models.BooleanField()
    b_bsp = models.BooleanField()
    b_wpd = models.BooleanField()

    create_date = models.DateTimeField()

    cost = models.IntegerField()


