from selenium import webdriver
import time

driver = webdriver.Chrome()
# 设置页面加载时间  【加载完成之后等待的时间 （有些动态页面，需要等待加载完成再抓取）】
driver.implicitly_wait(time_to_wait=10)
driver.get('http://www.jd.com')

# 操作滚动条 区间 在浏览器中查看 要爬取页面的高度：h      console命令：Math.max(h, h1)
# js = 'window.scrollTo(0, 1000)'
# js = 'window.scrollTo(0, 1000)'
# driver.execute_script(js)
# 不同的浏览器 document 不一样
js = 'window.scrollTo(0, Math.max(document.documentElement.clientHeight,document.body.clientHeight))'

driver.execute_script(js)

html_doc2 = driver.page_source
print(len(html_doc2))

# 关闭
driver.quit()