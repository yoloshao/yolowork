import threading
import time
def fetch(url):
    # lock.acquire()
    print(threading.enumerate())
    time.sleep(5)
    # lock.release()
    print(url)
    print(threading.enumerate())
# 源码中 target=None 为默认 不会调用
# lock = threading.Lock()

# 守护为True 主线程瞬间结束，线程强制结束
t1 = threading.Thread(target=fetch, args=('http://www.baidu.com',))
t1.daemon = False

t2 = threading.Thread(target=fetch, args=('http://www.so.com',))
t2.daemon = True

t1.start()
t2.start()
# print(threading.enumerate())