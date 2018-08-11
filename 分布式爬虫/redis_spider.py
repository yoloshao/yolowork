"""
爬虫：
    for url in urls:
        url 发送请求 获得response响应  解析response 保存数据
多线程爬虫:
    urls 保存在本地内存中
    work(url 发送请求 获得response响应  解析response 保存数据)
    启用多个work
多线程分布式爬虫:
    urls 保存在redis 内存数据库中
    多台电脑 从redis 内存数据库取URL，
    每台电脑执行的操作是：work(url 发送请求 获得response响应  解析response 保存数据)
"""
import sys
import time
from redis import Redis
import threading
import requests
from lxml import etree
IDLE = 0 # 空闲状态
WORKING = 1 # 工作状态
REDIS_SPIDER_KEY = 'spider:urls'
start_url = 'http://www.sohu.com'
# 过滤
ALLOW_DOMAIN = 'sohu.com'
MAX_DOWNLOAD_THREAD = 10

RETRY_TIME = 3 # 重置次数
TIME_OUT =5 # 超时时间

crawled_url = set() # 爬取过的url
REDIS_CRAWLED_URL = 'crawled_url'
rds = Redis('127.0.0.1', 6379)

# 重置次数
class Retry(object):
    def __init__(self, retries = RETRY_TIME):
        pass
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            pass
        return wrapper

def fetch(url):
    """
    下载页面，如果下载成功，返回网页源码 -- str
    :param url:
    :return: 返回str 类型的网页内容 或者 None
    """
    # 如果是新url, 就下载url 对应的页面，如果url 已经爬取过，忽略
    print(url)
    print(rds.smembers(REDIS_CRAWLED_URL))
    if rds.sadd(REDIS_CRAWLED_URL, url) == 1:
        print('Start fetching ..{url}'.format(url=url))
        # python 3.6 可以简写
        print(f'Start fetching..{url}')
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.text
    return None
    # else:
    #     pass


def parse(html):
    """
    解析html, 从html 中抽取新的url,
    :param html:
    :return: 返回值是一个list类型的url
    """
    if html is None:
        return None
    tree = etree.HTML(html)
    urls = tree.xpath('//a/@href')
    new_urls = []
    for url in urls:
        if ALLOW_DOMAIN in url:
            if url.startswith('http') or url.startswith('https'):
                new_urls.append(url)
    if not new_urls:
        return None
    return new_urls

class Spider(threading.Thread):
    """
    爬虫器
    """
    def __init__(self):
        super(Spider, self).__init__()
        # 初识状态是空闲
        self.status = IDLE
    def run(self):
        # blpop 等待取值 可以设置等待时间 查看源码
        while True:
            # 从redis url 队列中取出一个url, 如果队列中暂时没有url, 等待
            # 返回的是一个元组，下标0代表键，下标1代表url
            url = rds.blpop(REDIS_SPIDER_KEY)[1]
            # print(url)
            # print('hello')
            # 开始爬取url 对应的页面
            self.status = WORKING
            # 获取网页源码
            html = fetch(url)
            # 解析  获取页面中的url 并去重
            urls = parse(html)
            print(urls)
            if urls is not None:
                new_urls = set(urls)
                # lpush 会把urls 解成多个value 左到右依次传入
                rds.lpush(REDIS_SPIDER_KEY, *new_urls)
                # 等价
                # for url in urls:
                #     rds.lpush(REDIS_SPIDER_KEY, url)
                # 线程爬取结束
                self.status = IDLE
def all_is_idle(spiders):
    """
    检测所有爬虫线程是否均为空闲状态，如果都是空闲状态返回True,否则返回False
    :param spiders: 所有爬虫线程
    :return:bool
    """
    # spiders_status = []
    # for spider in spiders:
    #     spider.status.append(spiders.status)
        #等价
    spiders_status = [spiders.status for spider in spiders]
    # 内置方法all()    全部True 为True 否则为 False
    # 内置方法any()
    return any(spiders_status)

    # 另外一种方法
    # for spider in spiders:
    #     if spider.is_idle is not True:
    #         return False
    # return True

# 爬虫的入口
def main(n):
    rds.lpush(REDIS_SPIDER_KEY, start_url)
    # 创建n 个线程
    spider_pools = []
    for i in range(n):
        spider = Spider()
        spider_pools.append(spider)

    for spider in spider_pools:
        spider.start()
    while True:
        # 监听 rds 中的带爬取队列
        # 如果带爬取队列为空，结束爬虫
        if rds.llen(REDIS_SPIDER_KEY) == 0 and all_is_idle(spider_pools): # 退除系统会出问题 需要等到爬取结束
            print('所有线程爬取完毕.')
            sys.exit(0)
        else:
            time.sleep(2)

if __name__ == '__main__':
    main(MAX_DOWNLOAD_THREAD)
