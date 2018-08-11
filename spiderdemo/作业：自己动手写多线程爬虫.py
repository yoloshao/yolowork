# 队列模块
from queue import Queue
import threading
import requests
import re

start_url = "http://wwwgeyanw.com"
# 队列，存放要爬取的url
urls_queue = Queue()
# 并发下载线程数
DOWNLOADER_NUM = 10
# 线程池
thread_pool = []
