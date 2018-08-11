import asyncio
# 创建一个类，做汉堡的类
class Hamburger:
    @classmethod
    def make(cls,n,*args,**kwargs):
        """
        创建指定个数的对象
        """
        hamburgers = []
        for i in range(n):
            # 创建对象
            hamburgers.append(cls.__new__(cls,*args,**kwargs))
        return hamburgers
# 创建实例，一个实例就相当于一个汉堡
hamburges = Hamburger.make(5)
print(hamburges)
# 开始，已经做好了5个汉堡
async def make_hamburger(n):
    # 统计做的汉堡的个数
    count = 0
    while True:
        if len(hamburges) == 0:
            # 如果没有汉堡，根据请求做汉堡
            await ask_for_hamburger()
        # 取出一个汉堡给顾客
        hamburge = hamburges.pop()
        yield hamburge
        count += 1
        # 如果n 个汉堡都做好了，结束循环
        if count == n:
            break
async def ask_for_hamburger():
    await asyncio.sleep(2)
    hamburges.extend(Hamburger.make(8))
async def buy_hamburgers():
    bucket = []
    make_hamburger(12)
    async for hamburge in make_hamburger(12):
        bucket.append(hamburge)
        print('买到第{0}个汉堡'.format(id(hamburge)))

# 事件循环
loop = asyncio.get_event_loop()
loop.run_until_complete(buy_hamburgers())
loop.close()