from multiprocessing import Queue, Process
import time
import os

# 生产
# 斐波那契数列
def product(queue):
    no = 1
    while True:
        print('生产了', no)
        queue.put(no)
        time.sleep(0.5)

# 消费
def consume(queue):
    pass

if __name__ == '__main__':
    # 设置队列最大值
    queue = Queue(maxsize=20)
    productProcess = Process(target=consume,
                             args=(queue,))
    consumeProcess = Process(target=consume,
                             args=(queue,))
    # 启动生产者和消费者进程
    productProcess.start()
    consumeProcess.start()

    # 等待所有的子进程回收
    productProcess.join()
    consumeProcess.join()
    print('主进程----')