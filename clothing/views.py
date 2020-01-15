import os

from django.shortcuts import render, redirect

# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.project import get_project_settings
from scrapy_redis import get_redis

# from scraper.spiders.marissa import MarissaSpider


def index(request):
    return render(request, 'clothing/index.html', {})


def url_to_redis(request):
    r = get_redis()
    # os.environ.setdefault("SCRAPY_SETTINGS_MODULE", "scraper.settings")

    # crawler_settings = get_project_settings()
    # crawler = CrawlerRunner(crawler_settings)
    # crawler.crawl(MarissaSpider)

    r.lpush(
        'marissa:start_urls',
        'https://www.marissacollections.com/shop/clothing.html?limit=9'
    )
    return redirect('clothing:catalog')


def clothing_list(request):
    return render(request, 'clothing/cloth_list.html', {})
