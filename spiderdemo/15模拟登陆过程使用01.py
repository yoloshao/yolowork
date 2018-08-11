import urllib.request
from http import cookiejar
import urllib.parse

url = 'http://127.0.0.1:8000/admin/'
values = {
# <input type="hidden" name="csrfmiddlewaretoken"
# value="g8h37VpymLkr2toaALqqrCs6Gt0NU2Uc9DM7Ko9DUFjXxkAPjujor4xcHnnIusFi">
    "csrfmiddlewaretoken" : '',
    'username': 'yolo',
    'password': 'yoloshao'
}
# 创建一个cookie 对象
cookie = cookiejar.CookieJar()
# 创建一个cookie 处理器
cookie_process = urllib.request.HTTPCookieProcessor(cookie)

# 创建一个opener
opener = urllib.request.build_opener(cookie_process)

with opener.open(url) as response:
    for item in cookie:
        # 查看所有属性
        values['csrfmiddlewaretoken'] = item.value
        print(dir(item))
        print(item.name)
        print(item.value)

data = urllib.parse.urlencode(values).encode('utf-8')
req = urllib.request.Request(url, data)
response = opener.open(req)
with open('admin.html', 'wb') as f:
    f.write(response.read())
print(response.read().decode('utf-8'))

print('--------------')
for item in cookie:
    # 应该显示的是sessionid 保持了登陆状态
    print(item.name, item.value)