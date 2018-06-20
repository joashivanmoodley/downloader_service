# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from file_processor.models import Queue
import json

@csrf_exempt
def process_data(request):
    '''
    add content to a queue to be processed at a later stage using a cron.
    '''
    if request.POST:
        download_type = request.POST.get('download_type', None)
        email_address = request.POST.get('email', None)
        data = request.POST.get('html', '')
        if download_type != 'pdf':
            data = request.POST.get('data', '')
        print data
        queue, created = Queue.objects.get_or_create(
            email_address=email_address,
            content=data,
            download_type=download_type
        )
        if queue:
            return HttpResponse(json.dumps({'status': 'success'}))
    return HttpResponse(json.dumps({'status': 'fail'}))    