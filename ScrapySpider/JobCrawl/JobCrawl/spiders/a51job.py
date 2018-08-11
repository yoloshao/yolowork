# -*- coding: utf-8 -*-
import scrapy
# 郑州：https://search.51job.com/list/170200,000000,0000,00,9,99,python,2,1.html
# 杭州：https://search.51job.com/list/080200,000000,0000,00,9,99,python,2,1.html

from JobCrawl.items import JobcrawlItem


class A51jobSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['51job.com']
    # start_urls = ['http://51job.com/']
    # 映射
    place_map = {
        '郑州': '170200',
        '杭州': '080200'
    }

    def __init__(self, **kwargs):
        super(A51jobSpider,self).__init__(**kwargs)
        # print(kwargs)
        self.place = kwargs.get('place')
        self.place_code = self.place_map[self.place]
    def start_requests(self):
        urls = ['https://search.51job.com/list/{place_code},000000,0000,00,9,99,python,2,1.html'
                      .format(place_code=self.place_code)]
        print('self.place is:', self.place)
        print('self.place_code:', self.place_code)
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        # //div[@id="resultList"]/div[@class="el"]

        result_list = response.xpath('//div[@id="resultList"]/div[@class="el"]')
        for result in result_list:
            # 工作名称
            print(result.extract())
            name = result.xpath('.//p/span/a/text()').extract_first().strip()

            # 公司名称
            company = result.xpath('.//span[@class="t2"]/a/text()').extract_first().strip()
            item = JobcrawlItem()
            item['name'] = name
            item['company'] = company
            yield item

        # for i in range(100):
        #     item = JobcrawlItem()
        #     item['name'] = 'job' + str(i)
        #     item['company'] = 'job' + str(i)
        #     print(item)
        #     yield item
        # print(response.url)
