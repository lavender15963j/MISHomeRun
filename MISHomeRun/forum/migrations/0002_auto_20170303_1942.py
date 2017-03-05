# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(related_name='message_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='parent',
            field=models.ForeignKey(related_name='article_parent', blank=True, to='forum.Article', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(related_name='article_author', to=settings.AUTH_USER_MODEL),
        ),
    ]
