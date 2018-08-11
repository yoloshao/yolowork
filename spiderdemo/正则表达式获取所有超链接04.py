import re

# wb 写入（会打开文件，没有写入内容时会清空文件）
with open('poxiao.html', 'r') as f:
    html = f.read()

# 定义一个匹配模式
pattern = re.compile(r'href="(/[a-z0-9-/]+(.html)?)"')

urls = pattern.findall(html)

for url in urls:
    # 获得的是个元组 可以通过下标获取完整 url
    print('http://www.poxiao.com' + url[0])
