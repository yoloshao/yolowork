import requests
url = 'http://mp4.vjshi.com/2018-07-21/939ea715612ca69475abf411745c5f60.mp4'
# stream 流 ，断点上传，断点下载概念 一部分一部分获取
filename = url.split('/')[-1]
r = requests.get(url, stream=True)
with open(filename, 'wb') as f:
    for chunk in r.iter_content(chunk_size=512):
        if chunk:
            f.write(chunk)
