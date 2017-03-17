#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Team(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True,
            height_field = "height_field",
            width_field = "width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    URL = models.URLField(max_length=200, null=True)
    Coach = models.CharField(max_length=20, null=True)
    date = models.DateTimeField(null=True)

    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

