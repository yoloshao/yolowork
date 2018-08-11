from threading import Thread, current_thread, Lock
import time
cnt = 0 # 全局变量
def countTime():
    global cnt
    # 获取当前线程名
    threadName = current_thread().name
    print(threadName, '-->开始计数：', cnt)
    while True:
            # 开始会自动加锁__enter__
            with Lock:
                if cnt >= 60:
                    break
                cnt += 1
                time.sleep(0.2)
                print(threadName, '-->计数：', cnt)


if __name__ == '__main__':
    print(current_thread().name, '-->开始计时')
    start_time = time.time()
    # 多线程
    ts = [Thread(target=countTime) for _ in range(3)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    delta_seconds = time.time() - start_time
    print(current_thread().name, '-->停止计时')
    print('用时{0}'.format(delta_seconds))