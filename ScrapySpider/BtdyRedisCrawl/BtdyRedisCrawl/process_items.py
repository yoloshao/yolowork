"""
把 redis 缓存中的数据，转存到mongoDB 或者 MySQL 中
"""

import pymysql
import pymongo
import json
from redis import Redis
from BtdyRedisCrawl import settings

# 1. 从redis 中取数据
rds = Redis(settings.REDIS_HOST, settings.REDIS_PORT)
# 示例：存储到MongoDB
client = pymongo.MongoClient(host='127.0.0.1', port=27017)
db = client['btdy']
collection = db['movies']

while True:
    _,item = rds.blpop(settings.REDIS_ITEMS_KEY)
    print(item)
    # json str 转化为字典
    dict = json.loads(item.decode())
    # 2. 把取出的数据存储到数据库中
    collection.insert(dict)


