
from collections import Counter, defaultdict, deque, OrderedDict

# 获取Counter 获取序列中每个元素出现的次数，元素为key 次数为value 返回字典结构
b = Counter('aaaabbbdceeedsdss')
print(b)
print(type(b))
d = dict(b)# 类型转化
print(type(d))


d1 = Counter([1, 2, 4, 3, 2, 1, 6, 2])
print(d1)

# deque 双向队列
# 将可迭代的数据转为双向队列
d2 = deque([1, 2, 'hello', 4])
print(d2)

d2.append(7)
d2.appendleft(0) # 在左边追加元素
print(d2)

print(d2.pop())
print(d2.popleft())   # 从左边去除元素
print(d2)

d2.extend(['a', 'b'])
d2.extendleft(['c', 'd']) #先加c 后加 d
print(d2)


d2.rotate(2)  # 循环移动正为右  负为左
print(d2)

# defaultdict 有缺省值（默认值得字典）

# 返回对应类型的空值   int 0   list  []
d3 = defaultdict(int)
d3['name'] = 'rose'
print(d3['name'])
print(d3['age']) # age 无对应值

d4 = defaultdict(lambda : 'abc') # 无参的匿名函数
print(d4['name'])

# OrderedDict 有序字典（实际字典是无序的）
# 验证无序
d5 = {}
d5['a'] = 1
d5['b'] = 2
d5['c'] = 3

d6 = {}
d6['c'] = 3
d6['b'] = 2
d6['a'] = 1
print(d5 == d6)
# 达到key值有序
d7 = OrderedDict()
d7['a'] = 1
d7['b'] = 2
d7['c'] = 3
d8 = OrderedDict()
d8['c'] = 3
d8['b'] = 2
d8['a'] = 1
print(d7 == d8)




