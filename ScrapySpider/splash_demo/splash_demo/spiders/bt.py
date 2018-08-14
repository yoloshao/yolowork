# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class BtSpider(scrapy.Spider):
    name = 'bt'
    allowed_domains = ['btbtdy.net']
    start_urls = ['http://btbtdy.net/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url,callback=self.parse)

    def parse(self, response):
        print(response.xpath('//title/text()').extract_first())
