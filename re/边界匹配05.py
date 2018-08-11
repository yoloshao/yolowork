
import re

# ^  表示以指定字符开头
m = re.search('^www','  q   www.baidu.com')
print(m)


# re.M 多行匹配
m1 = re.findall('^www', 'www.baidu.com\nwww.sina.com.cn', re.M)
print(m1)

# $ 以指定字符结尾
m2 = re.match('^1[3578]\d{9}$','13245893421')
print(m2)

#  判断是否是163的邮箱  @163.com
m3 = re.match(r'^\w+@163\.com$', 'shaoyongle@163.com')
print(m3)