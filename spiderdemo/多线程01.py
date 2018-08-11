# 多线程模块

import threading
import random
import time

# 定义一个线程的子类

class Job(threading.Thread):

    def __init__(self, name):
        # 重写线程的构造方法 一定要调用父类方法, 定义的属性  要看看 父类里面有没有防止重写
        super(Job, self).__init__()
        self.name = name

        pass
    def run(self):
        print('开始下载{0}'.format(self.name))
        download_time = random.randint(3, 8)
        time.sleep(download_time)
        print('下载结束{0}'.format(self.name))

task1 = Job(name='task1')
task2 = Job(name='task2')
task3 = Job(name='task3')

task1.start()
task2.start()
task3.start()