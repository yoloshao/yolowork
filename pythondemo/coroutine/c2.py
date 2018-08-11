import asyncio
@asyncio.coroutine
def hello(name):
    print('---start coroutine---', name)
    yield from asyncio.sleep(1)
    print('---end coroutine---', name)

if __name__ == '__main__':
    # 获取事件管理器（循环读取事件状态）
    loop = asyncio.get_event_loop()
    # 不能传递数据
    h = hello()
    # 运行协程
    loop.run_until_complete(h)
    # 关闭
    loop.close()
    print('over')