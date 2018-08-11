import random
import time


def fib(n):
    print(0)
    index = 0
    a, b = 0, 1
    while index < n:
        async_time = yield b # 等待外部接收b 的值，如果b 值被外部接收，则等待，外部发送过来的数据给async_time
        print('等待--》', async_time)
        time.sleep(async_time)
        a, b = b, a + b
        index += 1

if __name__ == '__main__':
    f = fib(10) # 调用协程函数（生成器）
    num = next(f) # 第一次接收协程的yield 返回的数据，协程等待发送的
    print('-->', num)
    while True:
        try:
            # 向协程发送的数据（async_time）, 等待协程的yield 返回数据
            num = f.send(random.uniform(1, 2))
            print('-->', num)
        except:
            break
    print('___over___')