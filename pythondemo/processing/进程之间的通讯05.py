# 管道pipe实现多进程之间的通信

from multiprocessing import Pipe, Process
import os
import random
import time

def productApple(conn):
    print(os.getpid(), '----正在生产苹果----')
    for i in range(10):
        nums = random.randint(10, 50)
        print(os.getpid(), '生产了', nums, '个苹果')
        conn.send(str(nums))  # 只是发送
        time.sleep(random.uniform(1, 2))
    conn.send('over')
    print(os.getpid(), '本次生产结束')

if __name__ == '__main__':
    # 获取半双工的管道（conn2 只发不收，conn1 只收不发）
    conn1, conn2 = Pipe(duplex=False)

    pApple = Process(target=productApple, args=(conn2,))
    pApple.start()# 启动进程
    # 通过管道另一个连接来收子进程发过来的消息
    ns = 0
    while True:
        msg = conn1.recv()
        if msg == 'over':
            break
        print('主进程：本次收到的苹果：', msg)

    print('主进程共收到苹果数：', ns)