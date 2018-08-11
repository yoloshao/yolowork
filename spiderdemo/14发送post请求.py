import urllib.request
import urllib.parse
url = 'http://127.0.0.1:8000/admin/'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
             "Chrome/66.0.3359.181 Safari/537.36"
}
values = {
    'username': 'yolo',
    'password': 'yoloshao'
}
# 对数据进行编码
data = urllib.parse.urlencode(values).encode('utf-8')
print(data)
# 创建一个对象
# 方法可以省略， 当没有data时默认用get
req = urllib.request.Request(url, data=data, headers=headers, method='POST')
with urllib.request.urlopen(req) as response:
    html = response.read()
with open('login.html', 'wb') as f:
    f.write(html)

# 需要使用cookie 模拟登陆