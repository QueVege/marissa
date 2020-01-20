# Parsing https://www.marissacollections.com/shop/clothing.html

## Pre-steps:

1. pip install -r requirements.txt
2. python manage.py runserver
3. redis-server

## Steps (run in different terminals):

1. python manage.py runserver
2. celery worker -A marissa --loglevel=info
3. scrapy crawl marissa


Go to 127.0.0.1:8000/ in your browser and click on button.
