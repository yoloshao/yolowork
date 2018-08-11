from selenium import webdriver
from scrapy.http import HtmlResponse  # 引用的库

driver = webdriver.Chrome()
url = 'http://www.btbtdy.net/btdy/dy13241.html'
driver.get(url)
# 页面内容
html_doc = driver.page_source
# 获取的页面封装成response 对象   中间件中 参数添加request
response = HtmlResponse(url=url, body=html_doc, encoding='utf-8')
link = response.xpath('//a[@class="d1"]/@href').extract_first()
print(link)
with open('dtdy.html', 'w', encoding='utf-8') as f:
    f.write(html_doc)
driver.quit()

# 添加到下载中间request 里面， 固定url需要替换成 request.url 示例：下载btmovie

# 实现无界面运行
# from selenium.webdriver.chrome.options import Options
# option = Options()
# option.add_argument('--headless')
# driver = webdriver.Chrome(chrome_options=option)
# 代替
# driver = webdriver.Chrome()
