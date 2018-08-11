from http import cookiejar
import urllib.request

# 创建一个cookie 对象
cookie = cookiejar.CookieJar()
print(cookie)
# 创建一个cookie 处理器
cookie_process = urllib.request.HTTPCookieProcessor(cookie)

# 创建一个opener
opener = urllib.request.build_opener(cookie_process)

with opener.open('http://127.0.0.1:8000/admin/') as response:
    print(response)
print(cookie)


# 保存cookie在一个文件中

# 创建一个cookie 对象    Mozilla 火狐浏览器 之后可以有save的方法
cookie = cookiejar.MozillaCookieJar('cookie.txt')
print(cookie)
# 创建一个cookie 处理器
cookie_process = urllib.request.HTTPCookieProcessor(cookie)

# 创建一个opener
opener = urllib.request.build_opener(cookie_process)

with opener.open('http://127.0.0.1:8000/admin/') as response:
    print(response)
print(cookie)
# 存
cookie.save()
# 加载
cookie.load('cookie.txt')
print(cookie)