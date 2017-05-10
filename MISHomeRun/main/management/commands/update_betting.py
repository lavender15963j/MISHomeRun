#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from django.core.management.base import BaseCommand
from django.utils import timezone
from customer2.models import PurchaseRecord, SystemGiveRecord, FakeNote
from main.models import User

class Command(BaseCommand):
    
    help = 'Update expired game.'
    
    def handle(self, *args, **options):
        nowtime = timezone.now()

        users = User.objects.all()

        for user in users:
            fakenotes = FakeNote.objects.filter(user=user)
            for note in fakenotes:
                if not note.betting.game.is_final:
                    continue

                reason = None
                coin = 0

                if note.is_win_lp():
                    coin += 2
                if note.is_win_nlp():
                    coin += 2
                if note.is_win_bs():
                    coin += 2
                if note.is_win_wpd():
                    coin += 4
                
                if note.create_date < note.betting.game.date + datetime.timedelta(hours=-1):
                    coin += 1
                    reason = '提早1小時投注，金幣+1'
                
                if not SystemGiveRecord.objects.filter(receiver=user, note=note).exists():
                    record = SystemGiveRecord(
                        receiver=user,
                        note=note,
                        give_coins=coin,
                        reason=reason,
                        w_lp=note.is_win_lp(),
                        w_nlp=note.is_win_nlp(),
                        w_bs=note.is_win_bs(),
                        w_wpd=note.is_win_wpd(),
                    )
                    record.save()
                    user.coin = user.coin + coin
                    user.save()
                    print user.username, '+', coin
    print 'All OK!!!'