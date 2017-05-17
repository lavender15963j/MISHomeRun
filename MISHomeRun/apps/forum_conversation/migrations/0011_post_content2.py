# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('forum_conversation', '0010_auto_20170120_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content2',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='Description', blank=True),
        ),
    ]
