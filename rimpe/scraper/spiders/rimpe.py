from scrapy import Spider
from scrapy.loader import ItemLoader
from scraper.items import ScraperItem


class RimpeSpider(Spider):
    name = "rimpe"
    allowed_domains = ["www.sri.gob.ec"]
    start_urls = ["https://www.sri.gob.ec/en/rimpe"]

    def parse(self, response):
        for link in response.xpath("/html//div[@id = '¿quiénes']//a"):
            loader = ItemLoader(item=ScraperItem(), selector=link)
            url = link.xpath(".//@href").extract_first()
            loader.add_value("file_urls", url)
            yield loader.load_item()
