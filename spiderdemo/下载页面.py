import requests
# 引入模块 能指定文件编码
import codecs
def fetch(url):
    """
    获取url对应页面的内容
    参数：url
    返回值：
    如果页面成功获取，以str类型返回页面内容，否则返回None
    """
    # r 对象
    r = requests.get(url)
    if r.status_code is 200:
        return r.content
        # r.text str 类型 用w 写入
        # 如果用r.content 二进制类型 后面用wb 二进制写入
    return None
def main():
    result = fetch('https://www.poxiao.com/')
    if result is None:
        return '获取页面失败'
    else:
        # 编码 出现乱码可以看原网页的编码方式
        with open('poxiao.html', 'wb') as f:
            f.write(result)
        return '下载完成'
if __name__ == '__main__':
    print(main())