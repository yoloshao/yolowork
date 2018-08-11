
import re
#　分割多个空格的字符串
l = re.split(' +', 'my name  is   zhangsan')

print(l)



l1 = re.split('[ ,]+', 'my name  is   zhangsan,hello world')
print(l1)

# sub 替换，第二个参数表示替换的内容
s = re.sub('\d+','****','zhangsan576898098080lisi7799889')
print(s)

# 通过count参数，可以指定替换的个数
s1 = re.sub('\d+','****','zhangsan576898098080lisi7799889', count=1)
print(s1)

info = '我我我我没有学学学会正正正则'
pattern =r'(.)\1+'
info1 = re.sub(pattern, r'\1', info)
print(info1)