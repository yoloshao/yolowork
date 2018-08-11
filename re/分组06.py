

import re

m = re.match('[hH]ello', 'hello')
print(m)
# | 或的意思  () 分组
m1 = re.match('(h|H)ello', 'hello')
print(m1)
print(m1.group())  # 查看匹配内容
print(m1.group(1))   # 获取匹配的第一个分组的内容




#<html>safasfa</html>
# 查看是否符合 要求

m2 = re.match(r'<\w+>.*</\w+>','<html>safasfa</html>')

# \1 表示第一个分组匹配的内容
m3 = re.match(r'<(\w+)>.*</\1>','<html>safasfa</html>')
print(m2)
print(m3)
print(m3.group(0))
print(m3.group(1))

# (?p<分组名>....)      使用时（?p=分组名）
m4 = re.match(r'<(?P<name1>\w+)>(.*)</(?P=name1)>','<html>safasfa</html>')
print(m4)
# 根据分组名得到匹配的内容
print(m4.group('name1'))
