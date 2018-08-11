import queue
import random
from threading import Thread, current_thread
import time

# 任务线程
class Work():
    def __init__(self, work_queue):
        self.work_queue = work_queue
        self.start()   # 启动线程
    def run(self):
        # 不停地取到任务，并执行任务
        while True:
            try:
                task_func, args = self.work_queue.get(block=False)
                task_func(*args)
            except:
                break


# 任务线程管理器-线程池管理器
class WorkPool:
    def __init__(self, task_nums, pool_size=10):
        self.task_queue = queue.Queue()  # 任务 队列
        self.thread_pool = None
        self.task_nums = task_nums
        self.init_pool(pool_size) # 初始化线程池
        self.init_tasks() # 
    def init_pool(self, pool_size):
        pool_size = pool_size if self.task_nums > pool_size else self.task_nums
        for i in range(pool_size):
            # 初始化线程池
            self.thread_pool.append(Work(self.task_queue))

    def init_tasks(self):
        # 向任务队列中添加任务
        for i in self.task_nums:
            self.task_queue.put((do_task, (i, random.choice(worker_names))))

    def wait_allcomplete(self): # 等待所有的线程池，都完成任务
        for work in self.task_queue:
            # isAlive = is_Alive
            if work.isAlive():
                work.join()
                print('---all work completed')

worker_names = ['李sir', '王sir', 'Miss王']

def do_task(*args):
    time.sleep(0.1)
    print(current_thread().name, '---->', *args)

if __name__ == '__main__':
    print('--开始使用自定义的线程池--')
    pool = WorkPool(5)
    pool.wait_allcomplete()
    # 一个是使用函数
    # pool.apply_async(Work())
    print('--所有任务都已经完成--')

