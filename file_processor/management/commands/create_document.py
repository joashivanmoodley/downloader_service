from django.conf import settings
from django.core.management.base import NoArgsCommand
from weasyprint import HTML
from file_processor.models import Queue


class Command(NoArgsCommand):

    def create_pdf_files(self):
        for queue in Queue.objects.filter(sent=False):
        	email_address = queue.email_address
			html = queue.html
			HTML(string=html).write_pdf('assets/%s.pdf' % email_address.replace('.', '_'))
    def create_xls_files(self):
        pass

    def handle_noargs(self, **options):
        self.create_pdf_files()
        self.create_xls_files()