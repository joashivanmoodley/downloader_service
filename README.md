# downloader_service
Microservice to handle the creation of pdfs and xls docs.

Setup:
pip install requirements.tx
create db
python manage.py migrate

These is a management command that should be set to run on prod to actually create the doc and send it. When A request comes to generate a file, the content is then added to the queue which waits till the cron runs to physically generate the file.
