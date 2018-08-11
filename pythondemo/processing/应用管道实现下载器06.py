# 应用管道实现下载器（Downloader功能）

import requests
from multiprocessing import Pipe, Process


def downloader(conn):
    # 扩展： 设置超时时长为 60s
    # 如果60s 内没有任务到达，则关闭下载器

    while True:
        url = conn.recv() # 接收下载任务
        resp = requests.get(url)
        if resp.status_code == 200:
            # 回发下载的任务
            conn.send(resp.content)
        else:
            conn.send('下载失败'.encode())
if __name__ == '__main__':
    conn1, conn2 = Pipe()
    downloadProcess = Process(target=downloader,
                              args=(conn1,))
    downloadProcess.start()
    start_urls = ['http://www.baidu.com',
                  'http://www.jd.com',
                  'http://www.163.com']
    for url in start_urls:
        conn2.send(url)
        response = conn2