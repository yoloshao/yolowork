
import re

# * 表示前面的字符出现0次或多次   0次返回空
m = re.match('\d*', '12345')
print(m)
# 表示前面字符出现至少1次   不出现返回None
m1 = re.match('\d+', '12345')
print(m1)

# 表示前面字符返回0次或1次    0次返回空
m2 = re.match('\d?', '12345')
print(m2)

# 匹配0-99 范围内的数字字符
c = re.match('\d?\d', '78')
print(c)
c1 = re.match('\d?\d', '8')
print(c1)

c2 = re.match('\d\d?', '87999999')
print(c2)


print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
# 贪婪
# {} 匹配次数  少于指定次数返回None
w =re.match('\d{6}', '1234567890')
print(w)
# 至少匹配次数 （指定范围）
w1 =re.match('\d{6,10}', '1234567')
print(w1)


# 匹配座机号 0371-66666666
pattern = r'0[1-9]\d{1,2}-\d{7,8}'
l = re.match(pattern, '0371-88888888')
print(l)


