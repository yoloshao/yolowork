

import itertools
# 从n个元素中取出m个排列
# 排列 （有顺序要求）
it1 = itertools.permutations([1, 2, 3, 4], 2)
# 不能直接输出
print(it1)

for v in it1:
    print(v)
print('-----------------------------------------------')
# 无顺序要求   组合
it3 = itertools.combinations([1, 2, 3, 4], 2)

for v in it3:
    print(v)


it4 = itertools.combinations('abcd', 2)

for v in it4:
    print(v)


# 笛卡尔积， 得到多个序列中所有可能的排列组合

it5 = itertools.product([1, 2, 3], [1, 2, 3], [1, 2, 3])
for v in it5:
    print(v)

# 6次方
it6 = itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=6)

for v in it6:
    print(v)
