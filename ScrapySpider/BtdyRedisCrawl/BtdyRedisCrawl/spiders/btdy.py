# -*- coding: utf-8 -*-
import scrapy
# 导入分布式爬虫模块
from scrapy_redis.spiders import RedisSpider
from BtdyRedisCrawl.items import BtdyrediscrawlItem

from redis import Redis
# 直接引用setting 的设置也可以
from BtdyRedisCrawl import settings
# 继承分布式爬虫
class BtdySpider(RedisSpider):
    name = 'btdy'
    # allowed_domains = ['btbtdy.net']
    # start_urls = ['http://btbtdy.net/']
    redis_key = 'btdy:start_urls'
    def __init__(self):
        super().__init__()
        rds = Redis(settings.REDIS_HOST,settings.REDIS_PORT)
        urls = ['http://www.btbtdy.net/btfl/dy1-{0}.html'.format(str(page + 1)) for page in range(62)]
        rds.lpush(self.redis_key, *urls)

    def parse(self, response):
        # print(response.xpath('//title').extract_first())
        movies = response.xpath('//div[@class="cts_ms"]')
        for movie in movies:
            name = movie.xpath('.//p[@class="title"]/a/text()').extract_first()
            score = movie.xpath('.//p[@class="title"]/span/text()').extract_first()
            category = movie.xpath('.//p[@class="des"]/text()').extract_first()
            print(name, score, category)
            item = BtdyrediscrawlItem
            item['name'] = name
            item['score'] = score
            item['category'] = category
            print(item)
            yield item
