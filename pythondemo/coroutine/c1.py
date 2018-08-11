def fib(n):
    res = [0]
    index = 0
    a, b = 0, 1
    while index < n:
        res.append(b)
        a, b = b, a + b
        index += 1
    return res

if __name__ == '__main__':
    for i in fib(10):
        print(i)