# 导入进程模块
from multiprocessing import Process
import time
from random import randint
import os
def coding():
    # 编写代码的进程
    while True:
        print('开始写代码...')
        time.sleep(randint(3, 8))
        print('结束写代码...')
def thinking():
    # 思考的进程
    while True:
        print('开始思考...')
        time.sleep(randint(3, 8))
        print('结束思考')

if __name__ == '__main__':
    # 创建进程
    p1 = Process(target=coding)
    p2 = Process(target=thinking)
    # 启动进程
    p1.start()
    # 进程阻塞 必须在启动之后 必须完成才会进行(优先级)别的工作
    p1.join()
    p2.start()
    while True:
        time.sleep(randint(3, 8))
        print('主进程的pid是：{pid}'.format(pid=os.getpid()))
