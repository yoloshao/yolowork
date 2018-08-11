
# 相邻两个依次比较   冒泡

l = [12, 6, 34, 32, 25]

count = len(l)

for i in(0, count - 1):
    for j in range(0, count - 1):
        if l[j] > l[j + 1]:
            l[j],l[j + 1] = l[j + 1],l[j]
print(l)
