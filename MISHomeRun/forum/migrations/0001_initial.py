# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(related_name='article_parent', blank=True, to='forum.Article', null=True)),
                ('user', models.ForeignKey(related_name='article_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(related_name='article', to='forum.Article')),
                ('user', models.ForeignKey(related_name='message_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
