# -*- coding: utf-8 -*-
import scrapy
# 通用爬虫类 指定爬虫规则
from scrapy.spiders import CrawlSpider,Rule
# 链接提取器， 默认提取所有链接
from scrapy.linkextractors import LinkExtractor

# 继承通用
class SohuSpider(CrawlSpider):
    name = 'sohu'
    # allowed_domains = ['www.dushu.com']
    start_urls = ['http://www.dushu.com/']
    # 指定规则
    rules = (
        # 元组需要加标点 () 里可以放过滤条件 xpash css 正则
        # Rule(LinkExtractor(),follow=True),
        # Rule(LinkExtractor()),
        # Rule(LinkExtractor(restrict_xpaths=('//div[@class="news"]/p/a',)), follow=False, callback='self.parse_item'),

        Rule(LinkExtractor(allow=(r'/showbook/\d+')),callback='parse_item'),
        Rule(LinkExtractor(allow=(r'')),callback='parse_ssss'),
    )
    # follow = True 把请求返回的response 进一步提取url
    # follow = False 只解析一层url
    # 当有callback 时候，为False, 默认有callback 新的url 给予callback 解析

    # 通用爬虫源代码有parse函数，避免覆盖所以这里不能再使用
    def parse_item(self, response):
        print(response.xpath('//title/text()').extract_first())
        print('hello')
        
    def parse_ssss(self, response):
        pass
