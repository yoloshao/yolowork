
# 比较轮数 i
# 比较次数 j

l = [20, 23, 34, 12, 18]
n = len(l)
for i in range(0, n - 1):

    for j in range(i + 1, n):
        if l[i] > l[j]:
            l [i],l[j] = l[j],l [i]

print(l)
