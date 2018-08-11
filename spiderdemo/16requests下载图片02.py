import requests
url = 'http://img.zcool.cn/community/0100785859056fa8012060c8c2bbc0.JPG@1280w_1l_2o_100sh.jpg'
r = requests.get(url)
with open('demo.jpg', 'wb') as f:
    f.write(r.content)
# 下载会先放在内存中  大文件不能这样下载