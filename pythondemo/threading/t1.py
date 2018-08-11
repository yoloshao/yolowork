from threading import Thread, current_thread
import time
cnt = 0 # 全局变量
def countTime():
    global cnt
    # 获取当前线程名
    threadName = current_thread().name
    print(threadName, '-->开始计数：', cnt)
    while True:
        time.sleep(0.2)
        cnt += 1
        print(threadName, '-->计数：', cnt)
        if cnt >= 60:
            break

if __name__ == '__main__':
    print(current_thread().name, '-->开始计时')
    start_time = time.time()
    thread1 = Thread(target=countTime)
    thread1.start()
    # 等待子线程完成
    thread1.join()
    delta_seconds = time.time() - start_time
    print(current_thread().name, '-->停止计时')
    print('用时{0}'.format(delta_seconds))