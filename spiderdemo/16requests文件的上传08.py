import requests

url = ''
files = {
    # 键： 文件对象 二进制上传避免出现问题
    'file': open('somefile.txt', 'rb')
}
# 上传用post请求， url 服务器地址
r = requests.post(url, files=files)