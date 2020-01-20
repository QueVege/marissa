# Parsing https://www.marissacollections.com/shop/clothing.html

## Steps:

1. python manage.py migrate
2. python manage.py runserver
3. celery worker -A marissa --loglevel=info
4. scrapy crawl marissa

Go to 127.0.0.1:8000/ in your browser and click on button.
