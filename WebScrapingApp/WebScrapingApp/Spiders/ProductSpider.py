from itertools import count, product
from turtle import done
import scrapy
import time


class ProductsSpider(scrapy.Spider):
    name = "products"
    url = 'https://www.3djake.nl/filament'
    counter = 0
    done = False

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parseTypes)

    def parseTypes(self, response):
        for product in response.css('a.product__imagewrap::attr(href)').getall():
            if product is not None:
                product = response.urljoin(product)
                yield scrapy.Request(product, callback=self.parseProductList)
        self.counter = self.counter + 1
        next_page = self.url + '?page=' + str(self.counter)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parseTypes)
        if next_page is None:
            self.done = True
            

    def parseProductList(self, response):
        time.sleep(0.05)
        yield {
                'text': response.css('span.p-price__perunit::text').get(),
                'headers': response.css("div.product-properties:not([class*='hidden']) th::text").getall(),
                'values': response.css("div.product-properties:not([class*='hidden'])  td::text").getall(),
                'brand' : response.css(".product-properties:not([class*='hidden']) a::text").getall()[0],
                'material' : response.css(".product-properties:not([class*='hidden']) a::text").getall()[1]
            }
