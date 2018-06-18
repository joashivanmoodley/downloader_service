# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Queue(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    email_address = models.EmailField()
    html_content = models.TextField(blank=True, null=True)
    sent = models.BooleanField(default=True)
