# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from ckeditor_uploader.fields import RichTextUploadingField
from machina.apps.forum_conversation.abstract_models import AbstractPost
from django.utils.translation import ugettext_lazy as _
from machina.models.fields import MarkupTextField

# Custom models should be declared before importing
# django-machina models

class Post(AbstractPost):
    content2 = RichTextUploadingField(_('Description'))

from machina.apps.forum_conversation.models import *  # noqa