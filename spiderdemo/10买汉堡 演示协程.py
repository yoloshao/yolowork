def buy():
    result = ""
    while True:
        # yield 调用result 返回给r
        n = yield result
        if not n:
            return None
        result = '{n}购买成功'.format(n=n)
def make(buy):
    next(buy)
    n = 0
    while n < 5:
        n = n + 1
        # 协程工作
        r = buy.send(n)
        print(r)
    buy.close()
if __name__ == '__main__':
    buy = buy()
    make(buy)