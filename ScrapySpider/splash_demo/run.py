from scrapy import cmdline
# --nolog 代码异常会没有异常输出 最后再添加
# -o btdy.json 保存json 文件
# cmdline.execute('scrapy crawl 51job -a place=杭州 -a a=2 --nolog'.split())
cmdline.execute('scrapy crawl bt --nolog'.split())