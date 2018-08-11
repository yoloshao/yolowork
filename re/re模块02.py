
import re
# 第一个参数表示正则表达式的语法
v = re.match('www','www.baidu.com')
print(v)
print(type(v))

# match 从头开始判断字符串是否满足正则表达式的匹配规则
v1 = re.match('www','swww.baidu.com')
print(v1)

# 区分大小写              re.I (忽略大小写)
v2 = re.match('www','Www.baidu.com', re.I)
print(v2)
print(v2.group()) # 获取匹配的数据
print(v2.span())  # 获取匹配的数据的索引范围
# 查找 是否有满足正则表达式的内容  没有找到返回None
s = re.search('www','www.baidu.com')
print(s)
# 不在首位也可以
s1 = re.search('www','ssswww.baidu.com')
print(s1)
# 只查找第一个
s2 = re.search('www','ssswww.baiduwww.com')
print(s2)

# 查找所有满足规则的数据，将它们放入列表中返回
l = re.findall('www', 'www.baidu.com www.sina.com.cn')
print(l)

print('---------------------------------------------')

# compile的参数，表示正则表达式的匹配规则
pattern = re.compile('www')
m = pattern.match('www.baidu.com')
print(m)