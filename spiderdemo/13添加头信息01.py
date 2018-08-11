"""
User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36
"""
import urllib.request
url = 'http://www.douban.com'
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
             "Chrome/66.0.3359.181 Safari/537.36"
}
# 创建一个请求对象
req = urllib.request.Request(url,headers=headers)
# 发送请求对象
with urllib.request.urlopen(req) as response:
    html = response.read()
with open("douban.html", 'wb') as f:
    f.write(html)


