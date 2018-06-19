# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Queue(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    email_address = models.EmailField()
    content = models.TextField(blank=True, null=True)
    download_type = models.CharField(blank=True, null=True, max_length=100)
    sent = models.BooleanField(default=False)
