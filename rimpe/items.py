import scrapy

class SpiderItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()