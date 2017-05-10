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
    
    create_date = models.DateTimeField(auto_now_add=True)

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
    h_wpd1 = models.IntegerField(default=0)
    h_wpd2 = models.IntegerField(default=0)
    h_wpd3 = models.IntegerField(default=0)
    h_wpd4 = models.IntegerField(default=0)
    h_wpd5 = models.IntegerField(default=0)
    h_wpd6 = models.IntegerField(default=0)
    h_wpd7 = models.IntegerField(default=0)
    h_wpd8 = models.IntegerField(default=0)
    h_wpd9 = models.IntegerField(default=0)

    a_wpd1 = models.IntegerField(default=0)
    a_wpd2 = models.IntegerField(default=0)
    a_wpd3 = models.IntegerField(default=0)
    a_wpd4 = models.IntegerField(default=0)
    a_wpd5 = models.IntegerField(default=0)
    a_wpd6 = models.IntegerField(default=0)
    a_wpd7 = models.IntegerField(default=0)
    a_wpd8 = models.IntegerField(default=0)
    a_wpd9 = models.IntegerField(default=0)

    """
    @property
    def get_money(self):
        is_home_team_winner = self.betting.game.winner == True
        is_away_team_winner = not is_home_team_winner
        money = 0

        if self.betting.game.home_team_score > self.betting.game.away_team_score:
            lp = self.betting.game.home_team_score - self.betting.game.away_team_score
        else:
            lp = self.betting.game.away_team_score - self.betting.game.home_team_score

        if lp > self.betting.let_point_number:
            if is_home_team_winner:
                money += self.lp_home_team * self.betting.lp_home_team_odds
            if is_away_team_winner:
                money += self.lp_away_team * self.betting.lp_away_team_odds

        if is_home_team_winner:
            money += self.nlp_home_team * self.betting.nlp_home_team_odds
        if is_away_team_winner:
            money += self.nlp_away_team * self.betting.lp_away_team_odds

        allScore = self.betting.game.home_team_score + self.betting.game.away_team_score
        if allScore > self.betting.big_small_point_number:
            money += self.big * self.betting.big_odds
        else:
            money += self.small * self.betting.small_odds

        wpd = [self.wpd1, self.wpd2, self.wpd3, self.wpd4, self.wpd5, self.wpd6, self.wpd7, self.wpd8, self.wpd9,]
        odds = [self.betting.odds1, self.betting.odds2, self.betting.odds3, self.betting.odds4, self.betting.odds5, self.betting.odds6, self.betting.odds7, self.betting.odds8, self.betting.odds9,]
        for i in range(1, 10):   
            if lp > i:
                 money += wpd[i - 1] * odds[i - 1]

        return money
    """

    def __unicode__(self):
        return u"%s's Note For No.%d" % (self.user.username, 
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

    create_date = models.DateTimeField(auto_now_add=True)

    # Let Point
    lp_team = models.BooleanField()

    # No Let Point
    nlp_team = models.BooleanField()

    # No Let Point
    b_or_s = models.BooleanField()

    # Win Point Diff
    choice_team = models.BooleanField()
    wpd_num = models.IntegerField()

    def is_win_lp(self):
        is_home_team_winner = self.betting.game.winner == True
        is_away_team_winner = not is_home_team_winner

        if self.betting.game.home_team_score > self.betting.game.away_team_score:
            lp = self.betting.game.home_team_score - self.betting.game.away_team_score
        else:
            lp = self.betting.game.away_team_score - self.betting.game.home_team_score

        if lp >= self.betting.let_point_number:
            if self.lp_team == True:
                if is_home_team_winner:
                    return True
            if self.lp_team == False:
                if is_away_team_winner:
                    return True
        return False

    def is_win_nlp(self):
        is_home_team_winner = self.betting.game.winner == True
        is_away_team_winner = not is_home_team_winner

        if self.nlp_team == True:
            if is_home_team_winner:
                return True
        if self.nlp_team == False:
            if is_away_team_winner:
                return True

        return False

    def is_win_bs(self):
        allScore = self.betting.game.home_team_score + self.betting.game.away_team_score
        if allScore >= self.betting.big_small_point_number:
            bs = True
        else:
            bs = False
        if bs == self.b_or_s:
            return True
        return False

    def is_win_wpd(self):
        is_home_team_winner = self.betting.game.winner == True
        is_away_team_winner = not is_home_team_winner

        if self.choice_team == True:
            if not is_home_team_winner:
                return False
        if self.choice_team == False:
            if not is_away_team_winner:
                return False
        
        if self.betting.game.home_team_score > self.betting.game.away_team_score:
            temp = self.betting.game.home_team_score - self.betting.game.away_team_score
        else:
            temp = self.betting.game.away_team_score - self.betting.game.home_team_score
        
        if temp == self.wpd_num:
            return True
        return False


    """
    @property
    def get_coin(self):
        is_home_team_winner = self.betting.game.winner == True
        is_away_team_winner = not is_home_team_winner
        
        coins = 0

        if self.betting.game.home_team_score > self.betting.game.away_team_score:
            lp = self.betting.game.home_team_score - self.betting.game.away_team_score
        else:
            lp = self.betting.game.away_team_score - self.betting.game.home_team_score

        if lp > self.betting.let_point_number:
            if self.lp_team == True:
                if is_home_team_winner:
                    coins = coins + 1
            if self.lp_team == False:
                if is_away_team_winner:
                    coins = coins + 1

        if self.nlp_team == True:
            if is_home_team_winner:
                coins = coins + 1
        if self.nlp_team == False:
            if is_away_team_winner:
                coins = coins + 1

        allScore = self.betting.game.home_team_score + self.betting.game.away_team_score
        if allScore > self.betting.big_small_point_number:
            bs = True
        else:
            bs = False
        if bs == self.b_or_s:
            coins = coins + 1

        num = None
        for i in range(1, 10):
            if self.betting.game.home_team_score > self.betting.game.away_team_score:
                temp = self.betting.game.home_team_score - self.betting.game.away_team_score
            else:
                temp = self.betting.game.away_team_score - self.betting.game.home_team_score
            if  (temp > 0 and temp <=1) or (i == 9 and i > 1):
                num = i
                break
        
        if num == self.wpd_num:
            coins = coins + 1

        return coins
    """



class SystemGiveRecord(models.Model):
    receiver = models.ForeignKey(
        'main.User',
        on_delete=models.CASCADE,
        related_name='receiver',
    )

    note = models.ForeignKey(
        'customer2.FakeNote',
        on_delete=models.CASCADE,
        related_name='by_note',
        null=True,
    )

    create_date = models.DateTimeField(auto_now_add=True)

    give_coins = models.IntegerField()

    reason = models.TextField(blank=True, null=True)

    w_lp = models.BooleanField(default=False)
    w_nlp = models.BooleanField(default=False)
    w_bs = models.BooleanField(default=False)
    w_wpd = models.BooleanField(default=False)

class PurchaseRecord(models.Model):
    buyer = models.ForeignKey(
        'main.User',
        on_delete=models.CASCADE,
        related_name='buyer',
    )

    buy_note = models.ForeignKey(
        'customer2.FakeNote',
        on_delete=models.CASCADE,
        related_name='buy_note',
    )

    buy_for = models.CharField(max_length=5, null=True)

    

    create_date = models.DateTimeField(auto_now_add=True)

    cost = models.IntegerField()


