import scrapy
from scraper.items import Product
from scrapy_redis.spiders import RedisSpider


class MarissaSpider(RedisSpider):
    name = 'marissa'

    redis_key = 'marissa:start_urls'

    # start_urls = [
    #     'https://www.marissacollections.com/shop/clothing.html?limit=9'
    # ]

    def parse(self, response):
        products_urls = response.xpath(
            "//a[contains(@class, 'product-image')]/@href"
        ).extract()

        for url in products_urls:
            yield scrapy.Request(url=url, callback=self.callparse)

    def callparse(self, response):
        name = response.xpath(
            "//div[contains(@class, 'product-name')]/span/text()"
        ).extract_first()

        product = Product()
        product['name'] = name
        return product
