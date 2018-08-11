from threading import Thread, Lock
from queue import Queue

class VerifyIPThread(Thread):
    # 验证IP是否可用
    def __init__(self, lock, ipQueue):
        super().__init__()
        self.lock = lock
        self.ipQueue = ipQueue
    def run(self):
        # 从IP队列中读了爬取的代理IP，验证是否可用
        while not exitFlag:
            self.lock.acquire()
            if not self.ipQueue.empty():
                ip = self.ipQueue.get()
                print(self.name)