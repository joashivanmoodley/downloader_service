from django.conf import settings
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):

    def create_pdf_files(self):
        pass

    def create_xls_files(self):
        pass

    def handle_noargs(self, **options):
        self.create_pdf_files()
        self.create_xls_files()