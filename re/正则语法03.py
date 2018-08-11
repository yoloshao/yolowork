
import re
# 单字符匹配
# . 点表示除了\n 以外的任意的字符
m = re.match('.', 'abc')
m1 = re.match('.', '飞age')
# 返回None
m2 = re.match('.', '\n')
# re.S 也可以匹配\n
m3 = re.match('.', '\n', re.S)
# 返回多个
m4 = re.match('...', 'abcd')
print(m)
print(m1)
print(m2)
print(m3)
print(m4)

print('------------------------------')
v = re.match('[abc]', 'aba')
print(v)
# 匹配中括号中的任意一个字符
v1 = re.match('[abc]', 'bec')
print(v1)


v2 = re.match('[a-z]', 'good')
print(v2)
print('--------------')
v3 = re.match('[a-gm-z0-9]', 'zahag')
print(v3)

print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# \d  表示[0-9]  \D 表示匹配[0-9]以外的字符
m = re.match('\d', '1wer')
m1 = re.match('\D','wer')
# 等于\D
m2 = re.match('[^0-9]', 'zhaha')
print(m)
print(m1)
print(m2)

# 匹配空白字符
s = re.match('\s', ' 3245')
s1 = re.match('\s', '\t')
s2 = re.match('\s', '\n')
# 匹配非空白字符
s3 = re.match('\S', '\n')

print(s)
print(s1)
print(s2)
print(s3)

print('--------------------------------------')

j = re.match('\w', 'aadsf')
j1 = re.match('\w', '111dsf')
j2 = re.match('\w', '_adsf')
j3 = re.match('\w', '爱aadsf')
# j3 = re.match('\\w', '爱aadsf')  正确写法
# j3 = re.match(r'\w', '爱aadsf')  使用r后的写法

print(j)
print(j1)
print(j2)
print(j3)

print('////////////////////////////')
# \ 在正则表达式中也有特殊意义
# 编程语法中，\ 表示转义
h = re.match('D:\\\\重命名','D:\\重命名\\day01介绍')
h1 = re.match(r'D:\\重命名',r'D:\重命名\day01介绍')
print(h)
print(h1)

# 如果将一个\ 作为普通字符输出，正常来说需要使用\\
print('\t\\hafasdf')
# 在python 中，如果\ 和后面的字符不能表示一个已有的转义字符，那么这个\会作为一个普通的斜杠使用
print('\t\hafasdf')
# r 是raw（原生的）的简写   \ 相当于普通字符
print(r'\t\h1234')

# 使用r 前缀后，原来需要使用两个\\的地方，使用一个\ 就可以了