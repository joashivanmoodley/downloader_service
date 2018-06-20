from django.conf import settings
from django.core.management.base import BaseCommand
from weasyprint import HTML
from file_processor.models import Queue
from django.core.mail import EmailMessage
from email.mime.application import MIMEApplication

from datetime import datetime

import time
import xlwt
import json

class Command(BaseCommand):

    def create_pdf_files(self):
        '''
        gets all records that have not been sent and creates and send the pdf.
        '''

        try:
            for queue in Queue.objects.filter(sent=False, download_type='pdf'):
                email_address = queue.email_address
                html = queue.content
                timestamp = time.time()
                file_name = '%s_%s.pdf' % (str(timestamp).split('.')[0], email_address.replace('.', '_'))
                HTML(string=html).write_pdf('%s/%s' % (settings.MEDIA_ROOT, file_name))
                body=''' 
                Good Day,
                Please find your PDF request attached

                Regards
                Tagent Solutions
                '''
                msg = EmailMessage('Tagent Solutions PDF Download', body, settings.SERVER_EMAIL, [email_address])
                f = '%s/%s' % (settings.MEDIA_ROOT, file_name)
                with open(f, "rb") as pdf:
                    msg.attach(MIMEApplication(
                        pdf.read(),
                        Content_Disposition='attachment; filename="%s"' % file_name,
                        Name=file_name
                    ))
                msg.send()
                queue.sent = True
                queue.save()

        except Exception, e:
            print e
    def create_xls_files(self):
        '''
        gets all records that have not been sent and creates and send the xls.
        '''

        try:
            for queue in Queue.objects.filter(sent=False, download_type='xls'):
                email_address = queue.email_address
                data = json.loads(queue.content)
                timestamp = time.time()
                file_name = '%s_%s.xls' % (str(timestamp).split('.')[0], email_address.replace('.', '_'))
                workbook = xlwt.Workbook()
                sheet = workbook.add_sheet('Tagent Solutions')
                header_record = data[0].keys()

                for index, value in enumerate(header_record):
                    sheet.write(0, index, value)

                for index, value in enumerate(data):
                    for header_index, header_value in enumerate(header_record):
                        if header_value == 'user':
                            value[header_value] = '%s %s' % (value[header_value]['first_name'], value[header_value]['last_name'])
                        if header_value == 'position':
                            value[header_value] = '%s %s' % (value[header_value]['level'], value[header_value]['name'])
                        sheet.write(index+1, header_index, value[header_value])

                workbook.save('%s/%s' % (settings.MEDIA_ROOT, file_name))
                body=''' 
                Good Day,
                Please find your PDF request attached

                Regards
                Tagent Solutions
                '''
                msg = EmailMessage('Tagent Solutions XLS Download', body, settings.SERVER_EMAIL, [email_address])
                f = '%s/%s' % (settings.MEDIA_ROOT, file_name)
                with open(f, "rb") as pdf:
                    msg.attach(MIMEApplication(
                        pdf.read(),
                        Content_Disposition='attachment; filename="%s"' % file_name,
                        Name=file_name
                    ))
                msg.send()
                queue.sent = True
                queue.save()

        except Exception, e:
            print e

    def handle(self, *args, **options):
        self.create_pdf_files()
        self.create_xls_files()