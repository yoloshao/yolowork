import requests
# 访问页面有些必须登录就会重定向到登录页面
# r = requests.get('http://www.baidu.com', allow_redirects=False)# 禁用重定向
r = requests.get('http://www.taobao.com', allow_redirects=True) # 允许重定向

print(r.text)