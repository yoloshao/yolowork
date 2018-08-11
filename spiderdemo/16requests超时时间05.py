import requests
url='http://www.baidu.com'
try:
    r = requests.get(url=url, timeout=0.001)
except Exception as e:
    print('请求超时')
