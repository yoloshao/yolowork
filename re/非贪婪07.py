

# 正则中默认使用的是贪婪匹配，尽可能多的匹配字符

import re
s = 'nums contains 12 23 34'


m = re.match('.+(\d+ \d+ \d+)', s)

print(m)
print(m.group(1))
# 非贪婪匹配   针对* + ？ {}  后面使用？ 取消贪婪
m = re.match('.+?(\d+ \d+ \d+)', s)

print(m)
print(m.group(1))

m2 = re.match('[a-z]+\d+','abc123dfg')
print(m2)

m3 = re.match('[a-z]+\d+?','abc123dfg')
print(m3)

s = '<tr><td>123</td></tr><tr><td>erer</td></tr>'

l = re.findall('<tr>.*</tr>', s)
print(l)
# 如果使用分组，将分组中的内容放入列表中返回
l1 = re.findall('<tr>.*?</tr>', s)
print(l1)