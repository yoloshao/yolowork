import json
import requests

url = ''
user = {
    'username': 'yolo'
}
# 发送普通数据（json字符串）
requests.post(url, data=json.dumps(user))
# 发送json数据
requests.post(url, json)