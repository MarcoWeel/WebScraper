from Spiders.ProductSpider import ProductsSpider
import scrapy
import DataProcessor
from scrapy.crawler import CrawlerProcess
import os

process = CrawlerProcess(settings={
    "FEEDS": {
        "items.json": {"format": "json"},
    },
})

#make sure the file is deleted before starting
os.remove("items.json")

process.crawl(ProductsSpider)
process.start()


DataProcessor.start_processing()
