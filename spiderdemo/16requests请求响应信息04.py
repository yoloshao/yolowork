import requests

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
             "Chrome/66.0.3359.181 Safari/537.36"
}

resp = requests.get("http://www.baidu.com", headers=headers)
# 获得响应中的头信息
print(resp.headers)
# 也包含请求对象  可根据这个查找来源 进行反爬虫
# 在web view里 根据 user_agent = request.META.get('HTTP_USER_AGENT')
# 判断 请求对象的头 在不在user_agent里面
# 解决办法  伪造一个user_agent
print(resp.request.headers)
# 获得响应的内容，字符串格式
print(resp.text)
# bytes 格式
print(resp.content)
# 原始响应内容
print(resp.raw)
# json 格式 json() 代表的是方法  不是的强制转化会报错
print(resp.json())

