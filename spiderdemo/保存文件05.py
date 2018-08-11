import pymysql

from bs4 import BeautifulSoup

import pymysql.cursors

with open('poxiao.html', 'rb') as f:
    # 可以是文件对象
    # poxiao = BeautifulSoup(f)
    # 也可以是字符串（源代码字符串）
    # lxml 指定解析器 比较快
    poxiao = BeautifulSoup(f.read(), 'lxml')

# 获取文本
# print(poxiao.title.get_text())


# 从大块的div 中找到需要的模块
# div content clear  查找div  class为 content clear
content_div = poxiao.find(name='div', class_='content clear')
# print(content_div.text)
# print(type(content_div))
li_list = content_div.findAll(name='li')

# 连接数据库
# 客户端可以创建MySQL用户(% 会代表所有权限)


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='977557',
                             db='spider01',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


try:
    for li in li_list:
        href = li.a.get('href')
        title = li.get_text()

        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `movie` (`title`, `link`) VALUES (%s, %s)"
            cursor.execute(sql, (title, href))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
    # 从数据库读根据
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `title`, `link` FROM `movie` WHERE `movie_id`=%s"
        cursor.execute(sql, (1,))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()

