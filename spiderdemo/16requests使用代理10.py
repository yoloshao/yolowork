import requests
proxies = {
    'http': 'http://112.115.57.20:3128'
    # 'http': 'http://183.167.217.152:63000',
    # 'https': 'https://118.190.145.138:9001'
}
# 一个能查看本机ip 的网页 测试使用代理ip
r = requests.get('http://www.ip138.com/', proxies=proxies)
print(r.text)