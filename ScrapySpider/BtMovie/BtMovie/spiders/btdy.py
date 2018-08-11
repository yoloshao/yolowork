# -*- coding: utf-8 -*-
import scrapy
from BtMovie.items import BtmovieItem


class BtdySpider(scrapy.Spider):
    name = 'btdy'
    allowed_domains = ['btbtdy.net']
    start_urls = ['http://btbtdy.net/']

    def parse(self, response):
        # 从response 中提取请求头
        print(response.request.headers)
        # 从response 中提取所有的电影信息(电影名和二级页面的链接)
        movies = response.xpath('//div[@class="cts_ms"]/p/a')

        # 遍历所有的电影，把每一部电影的信息存入item, 然后yield item
        for movie in movies:
            href = movie.xpath('.//@href').extract_first()
            name = movie.xpath('.//text()').extract_first()
            # name_a = movie.attrib.get('title')
            # print(name)
            # print(href)

            # 创建一个item 对象, 用来存储一部电影信息
            item = BtmovieItem()
            item['name'] = name
            url = 'http://www.btbtdy.net' + href
            # item['link'] = href
            # print(item)
            req = scrapy.Request(url, callback=self.parse_movie_content, meta={'use_selenium':True, 'item': item})
            yield req
            break

    def parse_movie_content(self, response):
        # link = response.xpath('//a[@class="d1"]/@href').extract_first()
        # link 为None, 原因是网站有防爬虫策略，下载地址用的JavaScripy 动态加载
        # 处理方法：
        # 1.使用Selenium + Scrapy
        # 2.使用Splash + Scrapy
        # 假如测试

        item = response.meta.get('item')
        link = response.xpath('//ul[@class="p_list_02"]/li/span/a/@href').extract_first()
        item['link'] = link
        print(item)
        yield item
