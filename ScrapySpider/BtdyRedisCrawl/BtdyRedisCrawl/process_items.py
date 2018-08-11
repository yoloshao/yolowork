"""
把 redis 缓存中的数据，转存到mongoDB 或者 MySQL 中
"""

import pymysql
import pymongo
from redis import Redis
from BtdyRedisCrawl import settings

# 1. 从redis 中取数据
rds = Redis(settings.REDIS_HOST, settings.REDIS_PORT)
while True:
    _,item = rds.blpop(settings.REDIS_ITEMS_KEY)
    print(item)


