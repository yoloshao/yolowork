

# 深度遍历 （左下到右上） 广度遍历（从上到下）
import os

# 递归的写法体现了深度遍历的思想
def bianli(path):
    l = os.listdir(path)
    for v in l:
        p = os.path.join(path, v)
        print(p)
        if os.path.isdir(p):
            bianli(p)


# bianli('D:/重命名')


# 深度遍历

def deepth_bianli(path):

    stack = []
    stack.append(path)
    # 当栈中没有数据时候，表示遍历结束
    while len(stack) > 0:
        p = stack.pop()
        print(p)
        # 将文件夹下的内容先放进栈中
        if os.path.isdir(p):
            l = os.listdir(p)
            for v in l:
                pp = os.path.join(p, v)
                stack.append((pp))


# deepth_bianli('D:/重命名')

# 广度遍历

from collections import deque
def breadthbianli(path):
    # 队列中只存文件夹路径
    q = deque([])
    q.append(path)
    while len(q) > 0:
        # 从队列头取出数据
        p = q.popleft()
        if os.path.isdir(p):
            l = os.listdir(p)
            for v in l:
                pp = os.path.join(p, v)
                print(pp)
                if os.path.isdir(pp):
                    q.append(pp)
breadthbianli('D:/重命名')



