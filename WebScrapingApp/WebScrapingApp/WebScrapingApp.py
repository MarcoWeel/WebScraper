from Spiders.ProductSpider import ProductsSpider
import scrapy
import DataProcessor
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess(settings={
    "FEEDS": {
        "items.json": {"format": "json"},
    },
})

process.crawl(ProductsSpider)
process.start()


DataProcessor.start_processing()
