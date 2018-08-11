# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymongo

# 每次生成item 就执行一次
class JobcrawlPipeline(object):
    def process_item(self, item, spider):
        print(__file__, item)
        return item


    def close_spider(self, spider):
        print(__file__, spider.name)

# pip install pymysql
# db： 数据库
# table: 表名

class JobMySQLPipeline(object):
    # 连接数据库
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='977557',
            db='spider01',
            charset='utf8'
        )
        # 游标
        self.cursor = self.conn.cursor()

    # 插入数据库
    def process_item(self, item, spider):
        sql = "insert into jobs(`name`, company) values (%s, %s)"
        self.cursor.execute(sql, (item['name'], item['company']))
        # 提交
        self.conn.commit()
        return item
    # 关闭数据库连接(爬虫结束会关闭)
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

# mongo 数据存储
# class JobMongoPipeline(object):
#
#     def __init__(self):
#         # 创建一个Mongo的Client
#         self.client = pymongo.MongoClient(host='127.0.0.1',port=27017)
#         self.db = self.client['JobCrawl']
#         self.collection = self.db['jobs']
#     # 插入数据到数据库
#     def process_item(self, item, spider):
#         dict_item = dict(item)
#         self.collection.insert(dict_item)
#         return item
#
#     # 关闭数据库连接
#     def close_spider(self,spider):
#         self.client.close()
