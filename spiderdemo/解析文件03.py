from bs4 import BeautifulSoup

with open('poxiao.html', 'rb') as f:
    # 可以是文件对象
    # poxiao = BeautifulSoup(f)
    # 也可以是字符串（源代码字符串）
    # lxml 指定解析器 比较快
    poxiao = BeautifulSoup(f.read(), 'lxml')

# 获取文本
print(poxiao.title.get_text())


# 从大块的div 中找到需要的模块
# div content clear  查找div  class为 content clear
content_div = poxiao.find(name='div', class_='content clear')
# print(content_div.text)
# print(type(content_div))
li_list = content_div.findAll(name='li')
for li in li_list:
    print(li)
    print(li.a.get('href'))
    print(li.get_text())
    break