# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class EcommerceItem(scrapy.Item):
    short_title = scrapy.Field()
    full_title = scrapy.Field()
    memory = scrapy.Field()
    storage = scrapy.Field()
    color = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    site_name = scrapy.Field()