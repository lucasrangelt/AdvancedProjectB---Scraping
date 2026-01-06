import scrapy

class NotebookItem(scrapy.Item):
    full_title = scrapy.Field()
    memory = scrapy.Field()
    storage = scrapy.Field()
    color = scrapy.Field()
    price = scrapy.Field()