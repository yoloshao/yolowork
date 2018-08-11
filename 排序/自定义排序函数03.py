

l = [{'name':'Tom', 'age':10},
     {'name':'liming', 'age':30},
     {'name':'guoguo', 'age':50},
     {'name':'rose', 'age':18}]

count = len(l)

for i in range(0, count - 1):
    for j in range(0, count - 1 -i):
        if l[j]['age'] > l[j + 1]['age']:
            l[j],l[j + 1] = l[j + 1],l[j]


print(l)

sorted(l, key=lambda x:x['age'], reverse=True)

print('-------------------------------------------------')
def mysort(l, key, reverse):
    count = len(l)

    for i in range(0, count - 1):
        for j in range(0, count - 1 - i):
            if key == None:

                ret = l[j] > l[j + 1] if reverse == False else l[j] < l[j + 1]
            else:
                ret = key(l[j]) > key(l[j + 1]) if reverse == False else key(l[j]) < key(l[j + 1])
            if ret:
                l[j], l[j + 1] = l[j + 1], l[j]


mysort(l, key=lambda x:x['age'],reverse=True)
print(l)