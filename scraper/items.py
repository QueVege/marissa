# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    image = scrapy.Field()
    brand = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    options = scrapy.Field()
