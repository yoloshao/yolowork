import threading
def f():
    while True:
        x = yield
        print(x)
def func(g):
    next(g)
    g.send(10)
    next(g)
    g.send(12)

if __name__ == '__main__':
    g = f()
    print(threading.enumerate())
    func(g)