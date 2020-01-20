# Parsing https://www.marissacollections.com/shop/clothing.html

## Steps:

1. python manage.py migrate
   python manage.py runserver

2. celery worker -A marissa --loglevel=info

3. scrapy crawl marissa

Go to 127.0.0.1:8000/ in your browser and click on button.
