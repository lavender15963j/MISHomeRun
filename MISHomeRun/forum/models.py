#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Article(models.Model):
    user = models.ForeignKey(
        'main.User',
        on_delete=models.CASCADE,
        related_name='article_author',
    )

    parent = models.ForeignKey(
        'forum.Article',
        on_delete=models.CASCADE,
        related_name='article_parent',
        blank=True,
        null=True,
    )

    text = models.TextField()

    create_time = models.DateTimeField(auto_now=True)

class Message(models.Model):
    user = models.ForeignKey(
        'main.User',
        on_delete=models.CASCADE,
        related_name='message_author',
    )
    article = models.ForeignKey(
        'forum.Article',
        on_delete=models.CASCADE,
        related_name='article',
    )

    text = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
