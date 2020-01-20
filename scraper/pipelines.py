# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from clothing.tasks import add_to_db


class ScraperPipeline(object):
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        self.items.append(item._values)
        if len(self.items) >= 20:
            add_to_db.delay(self.items)
            self.items.clear()
        return item

    def close_spider(self, spider):
        if self.items:
            add_to_db.delay(self.items)
