import logging
# logging 记录（日志）
import time
from multiprocessing import Process
import os
import random

logging.getLogger().setLevel(logging.INFO)
def advanceArt(artId):
    logging.critical('---正在抢读---' + artId)
    time.sleep(10)
    if random.randint(0, 1) == 1:
        logging.critical('成功抢读')
    else:
        logging.critical('抢读失败')

if __name__ == '__main__':
    logging.info('...应用子进程来抢读...')
    # 创建子进程
    # advanceArt 函数对象
    process = Process(target=advanceArt,
                      kwargs={'artId': '1'})
    logging.info('is_alive' + str(process.is_alive()))
    # 启动子进程
    process.start()
    logging.warning('-----主进程over-------')

