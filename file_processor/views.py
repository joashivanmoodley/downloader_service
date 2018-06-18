# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from weasyprint import HTML
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from file_processor.models import Queue
import json
# Create your views here.

@csrf_exempt
def process_pdf(request):
    if request.POST:
        download_type = request.POST.get('download_type', None)
        email_address = request.POST.get('email', None)
        html = request.POST.get('html', '')
        queue, created = Queue.objects.get_or_create(
            email_address=email_address,
            html_content=html
        )
        HTML(string=html).write_pdf('assets/joash.pdf')
        if queue:
            return HttpResponse(json.dumps({'status': 'success'}))
    return HttpResponse(json.dumps({'status': 'fail'}))    