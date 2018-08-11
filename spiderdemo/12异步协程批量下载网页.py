"""
aiohttp  异步请求库
asyncio  异步协程库
re  正则表达式
async_timeout 用来设置异步超时时间
"""
import re
import asyncio
import aiohttp
import async_timeout

start_url = 'http://www.geyanw.com'
crawled_urls = []  # 已经爬过的url
ALLOW_HOST = 'geyanw.com'
async def start_reqeust():
    """
    根据start_url 获取网页的内容，从start_url 网页中
    提取新的url, 并把url 加到队列中
    :return:
    """
    # 以异步的方法获得网页内容
    content = await get_content(start_url)
    if content is not None:
        urls = parse_html(content)
        for url in urls:
            q.put_nowait(url)


async def get_content(url):
    """
    根据url 获取网页内容
    :param url: 网页地址
    :return:
    """
    async with aiohttp.ClientSession() as sesson:
        try:
            with async_timeout.timeout(5):
                async with sesson.get(url) as response:
                    if response.status == 200:
                        print("{url}下载成功".format(url=url))
                        html = await response.read()
                        return html
                    else:
                        return None
        except Exception as e:
            print(e)
        return None

def parse_html(html):
    """
    从html中提取新的url
    :param html:网页源码
    :return:网页源码中的所有url->list
    """
    pattern = re.compile(r'href="(/[a-z0-9-/]+(.html)?)"') # 匹配出来的是个元组
    urls = pattern.findall(html.decode('GBK'))
    return [start_url + url[0] for url in urls]
async def work(q):
    """
    从队列q 中取出url,以异步的方式发送一个get 请求，
    从返回的response中获取网页源码，从网页源码中提取url,
    如果url是新的没有爬过的有效url, 把url添加到队列中
    :param q:
    :return:
    """
    # while not q.empty():  都可以
    while True:
        # 从队列q 中取出url
        url = await q.get()
        if url not in crawled_urls:
            # 以异步的方式发送一个get 请求
            content = await get_content(url)
            if content is not None:
                urls = parse_html(content)
                for url in urls:
                    # 如果url 是新的没有爬过的有效url, 把url 添加到队列中
                    if url not in crawled_urls and ALLOW_HOST in url:
                        q.put_nowait(url)
            else:
                print("{url}请求失败".format(url=url))

if __name__ == '__main__':
    q = asyncio.Queue()
    loop = asyncio.get_event_loop()
    init_req = start_reqeust()
    task = asyncio.ensure_future(init_req)
    loop.run_until_complete(task)

    works = []
    # 创建多个协程
    for i in range(50):
        c = asyncio.ensure_future(work(q))
        # 把协程对象添加到列表
        works.append(c)

    loop.run_until_complete(asyncio.wait(works))
    loop.close()

    print(crawled_urls)