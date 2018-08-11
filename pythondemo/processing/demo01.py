# linux 才能运行fork
import os
import fork
import time

print('--尝试fork()进程--')
pid = fork()  # 返回0 代表子进程， 反之代表主进程
print('进程ID', os.getpid(), 'hello...')
