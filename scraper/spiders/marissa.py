import scrapy
from scraper.items import Product
from scrapy_redis.spiders import RedisSpider



class MarissaSpider(RedisSpider):
    name = 'marissa'

    redis_key = 'marissa:start_urls'

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

        image = response.xpath(
            "//img[contains(@itemprop, 'image')]/@src"
        ).extract_first()

        brand = response.xpath(
            "//div[contains(@class, 'designer-name')]/a/span/text()"
        ).extract_first()

        price = response.xpath(
            "//span[contains(@class, 'regular-price')]/span[contains(@class, 'price')]/text()"
        ).extract_first()

        description = response.xpath(
            "//dd[contains(@itemprop, 'description')]/p/text()"
        ).extract()

        product = Product()
        product['url'] = response.request.url
        product['name'] = name
        product['image'] = image
        product['brand'] = brand
        # product['category'] = category
        product['price'] = price
        product['description'] = description
        return product
