# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('forum_conversation', '0011_post_content2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content2',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Description'),
        ),
    ]
