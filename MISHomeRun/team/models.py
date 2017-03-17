#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Team(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

