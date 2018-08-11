"""
发送post 请求，字典会在请求时自动转化为表单
"""
import requests
url = 'http://127.0.0.1:8000/user/login/'
r = requests.post(url, data=dict(username='yolo', password='yoloshao'))
print(r.content)