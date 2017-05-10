#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from main.models import User
from customer2.models import SystemGiveRecord

class Command(BaseCommand):
    
    help = 'Update user record.'
    
    def handle(self, *args, **options):
        users = User.objects.all()

        for user in users:
            minSys = 1
            systems = SystemGiveRecord.objects.filter(receiver=user)
            length = len(systems)

            if not length >= minSys or length == 0:
                continue

            c_lp = 0
            c_nlp = 0
            c_bs = 0
            c_wpd = 0

            for s in systems:
                if s.w_lp:
                    c_lp += 1
                if s.w_nlp:
                    c_nlp += 1
                if s.w_bs:
                    c_bs += 1
                if s.w_wpd:
                    c_wpd += 1

            user.lp_wp = float(c_lp) / length * 100
            user.nlp_wp = float(c_nlp) / length * 100
            user.bs_wp = float(c_bs) / length * 100
            user.wdp_wp = float(c_wpd) / length * 100
            user.all_wp = (user.lp_wp + user.nlp_wp + user.bs_wp + user.wdp_wp) / 4
            user.save()
    print "All OK!!"

            
