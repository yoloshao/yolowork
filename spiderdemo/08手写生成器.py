# 手写形式
class My_gen(object):
    def __init__(self):
        self.number = 0
        pass
    def __next__(self):
        self.number += 1
        if self.number < 10:
            return self.number
        else:
            # 抛出异常 停止迭代
            raise StopIteration()
# 系统自带形式
def f():
    n = 0
    while n < 10:
        n += 1
        yield n
# 调用手写
g = My_gen()
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(next(g))
# 调用系统自带
h = f()
print(next(h))
print(next(h))
print(next(h))
print(next(h))