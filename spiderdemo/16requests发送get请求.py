import requests
r = requests.get('http://www.baidu.com/s',params={'wd':'python'})
# 等价
# requests.get('http://www.baidu.com/s',params=dict(wd='python'))

print(r)